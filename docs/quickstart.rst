====================
Guide de démarrage rapide
====================

Ce guide vous permet de démarrer rapidement avec OC Lettings en 5 minutes.

Installation rapide
===================

.. code-block:: bash

   # 1. Cloner le projet
   git clone https://github.com/votre-username/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR

   # 2. Créer et activer l'environnement virtuel
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate

   # 3. Installer les dépendances
   pip install -r requirements.txt

   # 4. Configurer la base de données
   python manage.py migrate

   # 5. Lancer le serveur
   python manage.py runserver

Accéder à l'application
========================

Page d'accueil
--------------
   http://127.0.0.1:8000/

Liste des locations
-------------------
   http://127.0.0.1:8000/lettings/

Liste des profils
-----------------
   http://127.0.0.1:8000/profiles/

Interface d'administration
---------------------------
   http://127.0.0.1:8000/admin/

.. note::
   Pour accéder à l'admin, un superutilisateur est mis a disposition:
    utilisateur: admin, mot de passe : Abc1234!

Commandes essentielles
=======================

Développement
-------------

.. code-block:: bash

   # Lancer le serveur de développement
   python manage.py runserver

   # Créer des migrations après modification des modèles
   python manage.py makemigrations

   # Appliquer les migrations
   python manage.py migrate

   # Créer un superutilisateur
   python manage.py createsuperuser

   # Collecter les fichiers statiques
   python manage.py collectstatic

Tests et qualité
----------------

.. code-block:: bash

   # Exécuter tous les tests
   pytest

   # Vérifier le linting
   flake8


Docker
------

.. code-block:: bash

   # Construire l'image Docker
   docker build -t oc-lettings:latest .

   # Lancer le conteneur
   docker run -p 8000:8000 oc-lettings:latest

   # Récupérer depuis Docker Hub
   docker pull ceorl/oc-lettings:latest
   docker run -p 8000:8000 ceorl/oc-lettings:latest

Structure du projet
===================

.. code-block:: text

   Python-OC-Lettings-FR/
   ├── doc/                      # Documentation Sphinx
   ├── lettings/                 # App Django - Locations
   │   ├── migrations/
   │   ├── templates/lettings/
   │   ├── tests/
   │   ├── admin.py
   │   ├── models.py
   │   ├── urls.py
   │   ├── apps.py
   │   └── views.py
   ├── profiles/                 # App Django - Profils
   │   ├── migrations/
   │   ├── templates/profiles/
   │   ├── tests/
   │   ├── admin.py
   │   ├── models.py
   │   ├── urls.py
   │   ├── views.py
   │   └── apps.py
   ├── oc_lettings_site/         # Configuration Django
   │   ├── migrations/
   │   ├── apps.py
   │   ├── asgi.py
   │   ├── tests.py
   │   ├── views.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── oc-lettings-site.sqlite3  # Base de donnée Sqlite3
   ├── static/                   # Fichiers statiques (CSS, JS, images)
   ├── templates/                # Templates HTML globaux
   ├── .github/workflows/        # CI/CD GitHub Actions
   ├── docker/                   # Fichier docker
   ├── requirements.txt
   ├── setup.cfg                 # Configuration flake8
   └── manage.py

Applications Django
===================

L'architecture est modulaire avec 3 applications :

**oc_lettings_site**
   Application principale contenant :

   - Configuration Django (``settings.py``)
   - Routing principal (``urls.py``)
   - Page d'accueil

**lettings**
   Gestion des locations immobilières :

   - Modèles : ``Address``, ``Letting``
   - URL : ``/lettings/``
   - Templates dans ``lettings/templates/lettings/``

**profiles**
   Gestion des profils utilisateurs :

   - Modèle : ``Profile``
   - URL : ``/profiles/``
   - Templates dans ``profiles/templates/profiles/``


Prochaines étapes
=================

- :doc:`usage` - Apprendre à utiliser toutes les fonctionnalités
- :doc:`database` - Comprendre la structure de la base de données
- :doc:`deployment` - Déployer l'application en production