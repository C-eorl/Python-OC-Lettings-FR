===================================
Procédures de déploiement
===================================

Cette section décrit le processus complet de déploiement de l'application
OC Lettings, depuis le développement local jusqu'à la production sur Render.

Vue d'ensemble du pipeline CI/CD
=================================

Architecture du pipeline
------------------------

.. code-block:: text

   ┌─────────────────┐
   │  Git Push       │
   │  sur GitHub     │
   └────────┬────────┘
            │
            ▼
   ┌─────────────────────────────────────────┐
   │     GitHub Actions (Workflow)           │
   ├─────────────────────────────────────────┤
   │                                         │
   │  Job 1: Build & Test                    │
   │  ├─ Linting (flake8)                    │
   │  ├─ Tests (pytest)                      │
   │  └─ Couverture > 80%                    │
   │          │                              │
   │          ▼ (si succès)                  │
   │                                         │
   │  Job 2: Containerize (branch main only) │
   │  ├─ Build image Docker                  │
   │  ├─ Tag: hash du commit                 │
   │  └─ Push vers Docker Hub                │
   │          │                              │
   │          ▼ (si succès)                  │
   │                                         │
   │  Job 3: Deploy (main only)              │
   │  └─ Déploiement sur Render (via hook)   │
   │                                         │
   └─────────────────────────────────────────┘

Déclenchement du pipeline
--------------------------

**Branche main** :

- Push → Jobs 1, 2 et 3 s'exécutent séquentiellement

**Autres branches** :

- Push → Job 1 uniquement (tests et linting)

Configuration du pipeline CI/CD
================================

Fichier de workflow GitHub Actions
-----------------------------------

**Emplacement** : ``.github/workflows/ci-cd.yml``

.. code-block:: yaml

   name: CI/CD Docker

    on: push

    jobs:

      test:
        runs-on: ubuntu-latest

        steps:
          - name: Checkout repo
            uses: actions/checkout@v4

          - name: Setup Python
            uses: actions/setup-python@v5
            with:
              python-version: "3.10"

          - name: Install dependencies
            run: |
              pip install -r requirements.txt

          - name: Run flake8
            run: flake8 .

          - name: Run pytest
            run: pytest


      docker:
        needs: test
        runs-on: ubuntu-latest
        environment: OC-Lettings
        if: github.ref == 'refs/heads/main'

        steps:
          - name: Checkout repo
            uses: actions/checkout@v4

          - name: Login DockerHub
            uses: docker/login-action@v4
            with:
              username: ${{ secrets.DOCKERHUB_USERNAME }}
              password: ${{ secrets.DOCKERHUB_TOKEN }}

          - name: Build image
            run: |
              docker build -f docker/Dockerfile \
                           -t ${{ secrets.DOCKERHUB_USERNAME }}/oc_lettings:latest \
                           -t ${{ secrets.DOCKERHUB_USERNAME }}/oc_lettings:${{ github.sha }} .

          - name: Push image
            run: |
              docker push ${{ secrets.DOCKERHUB_USERNAME }}/oc_lettings:latest
              docker push ${{ secrets.DOCKERHUB_USERNAME }}/oc_lettings:${{ github.sha }}

      renderhook:
        needs: docker
        runs-on: ubuntu-latest
        environment: OC-Lettings
        if: github.ref == 'refs/heads/main'

        steps:
          - name: Deploy on Render
            run: curl --fail -X POST ${{ secrets.RENDER_HOOK }}

Secrets GitHub à configurer
----------------------------

Dans ``Settings → Secrets and variables → Actions`` :

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Secret
     - Description
   * - ``DOCKERHUB_USERNAME``
     - Votre username Docker Hub
   * - ``DOCKERHUB_TOKEN``
     - Votre token d'accès Docker Hub
   * - ``RENDER_HOOK``
     - URL du webhook de déploiement Render


Conteneurisation Docker
=======================

Dockerfile
----------

**Emplacement** : ``docker/Dockerfile``

.. code-block:: dockerfile

    FROM python:3.10-slim
    LABEL authors="ceorl"
    LABEL description="OC Lettings Site"

    WORKDIR /app

    RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

    COPY requirements.txt ./
    RUN pip install --no-cache-dir -r requirements.txt
    RUN pip install --no-cache-dir gunicorn

    COPY .. .

    RUN python manage.py collectstatic --noinput


    CMD ["sh", "-c", "gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000 "]


Construction et test local
--------------------------

.. code-block:: bash

   # Construire l'image (être à la racine du projet)
   docker build -f docker/Dockerfile -t oc-lettings:local .

   # Lancer le conteneur
   docker run -p 8000:8000 oc-lettings:local

   # Accéder à l'application
   open http://localhost:8000

Récupération depuis Docker Hub
-------------------------------

.. code-block:: bash

   # Pull de l'image
   docker pull ceorl/oc_lettings:latest

   # Lancer en une commande
   docker run -p 8000:8000 ceorl/oc_lettings:latest

Déploiement sur Render
=======================

Configuration initiale
----------------------

**1. Créer un compte Render**

Aller sur https://render.com et créer un compte.

**2. Créer un nouveau Web Service**

- Dashboard → "New +" → "Web Service"
- Metter le lien vers votre image Docker

**3. Variables d'environnement**

Ajouter dans "Environment" :

.. code-block:: text

   SECRET_KEY=your-very-long-random-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=oc-lettings.onrender.com
   SENTRY_DSN=https://xxx@sentry.io/xxx

**4. Déploiement automatique**

Grace au hook de Render si L'image Docker change Rendre déploiera la nouvell image

Configuration du webhook de déploiement
----------------------------------------

Pour déclencher le déploiement depuis GitHub Actions :

1. Dans Render → Settings → "Deploy Hook"
2. Copier l'URL du webhook
3. L'ajouter comme secret GitHub : ``RENDER_DEPLOY_HOOK``


Surveillance avec Sentry
=========================

Configuration de Sentry
------------------------

**1. Créer un compte Sentry**

Aller sur https://sentry.io/signup/

**2. Créer un nouveau projet**

- Platform : Django
- Nom : OC Lettings
- Copier le DSN fourni dans le fichier .env


Flux de déploiement complet
============================

Workflow de développement à production
---------------------------------------

.. code-block:: text

   1. Développement local
      ├─ Créer une branche feature/xxx
      ├─ Développer et tester localement
      │  ├─ python manage.py runserver
      │  ├─ pytest
      │  └─ flake8
      └─ Commit et push

   2. Déploiement automatique
      ├─ Push sur main détecté
      ├─ Job 1 : Tests et linting ✓
      ├─ Job 2 : Build Docker et push ✓
      ├─ Job 3 : Déploiement sur Render ✓
      └─ Application en production

   3. Surveillance
      ├─ Sentry monitore les erreurs
      ├─ Logs accessibles sur Render
      └─ Tests manuels de vérification

Vérification du déploiement
----------------------------

Après un déploiement, vérifier :

**1. L'application est accessible**
    votre adresse Render:
    https://oc-lettings.onrender.com/

**2. Les fichiers statiques se chargent**

Ouvrir l'application dans le navigateur et vérifier :

- Le CSS s'applique correctement
- Le logo s'affiche
- Pas d'erreurs 404 dans la console

**3. L'admin fonctionne**

.. code-block:: bash

   open https://oc-lettings.onrender.com/admin/

**4. Les pages fonctionnent**

- ``/`` → Page d'accueil
- ``/lettings/`` → Liste des lettings
- ``/profiles/`` → Liste des profils

**5. Sentry reçoit des événements**

Vérifier dans le dashboard Sentry que l'application remonte des données.


Ressources et documentation
============================

- **Render** : https://render.com/docs
- **Docker** : https://docs.docker.com/
- **GitHub Actions** : https://docs.github.com/actions
- **Sentry** : https://docs.sentry.io/platforms/python/guides/django/
- **WhiteNoise** : http://whitenoise.evans.io/