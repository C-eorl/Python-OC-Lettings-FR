============
Installation
============

Cette section décrit les étapes nécessaires pour installer et configurer
OC Lettings en environnement de développement local.

Prérequis système
=================

Logiciels requis
----------------

- **Python 3.10 ou supérieur**
- **Git**

Vérification des prérequis
---------------------------

.. code-block:: bash

   # Vérifier la version de Python
   python --version
   # Résultat attendu : Python 3.10.x ou supérieur

   # Vérifier Git
   git --version
   # Résultat attendu : git version 2.30.x ou supérieur



Récupération du code source
============================

Cloner le dépôt Git
-------------------

.. code-block:: bash

   # HTTPS
   git clone https://github.com/C-eorl/Python-OC-Lettings-FR.git


   # Accéder au dossier du projet
   cd Python-OC-Lettings-FR

Configuration de l'environnement
=================================

Créer un environnement virtuel
-------------------------------

.. code-block:: bash

   # Créer l'environnement virtuel
   python -m venv venv

Activer l'environnement virtuel
--------------------------------


.. code-block:: bash
    # Linux / Mac
   source venv/bin/activate
    # Windows
   venv\Scripts\activate.bat


Installer les dépendances
--------------------------

.. code-block:: bash

   # Installer toutes les dépendances du projet
   pip install -r requirements.txt

Configuration de la base de données
====================================

Appliquer les migrations
-------------------------

.. code-block:: bash

   # Créer les tables de la base de données
   python manage.py migrate

Créer un superutilisateur (optionnel)
--------------------------------------

Pour accéder à l'interface d'administration :

.. code-block:: bash

   python manage.py createsuperuser

   # Suivre les instructions interactives :
   # - Username: admin
   # - Email: admin@example.com
   # - Password: (votre mot de passe sécurisé)

Variables d'environnement
==========================

Créer un fichier ``.env``
--------------------------

À la racine du projet, créer un fichier ``.env`` :

.. code-block:: bash

   # .env
   SECRET_KEY=votre-clé-secrète-django-très-longue-et-aléatoire
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   SENTRY_DSN=https://votre-dsn-sentry@sentry.io/projet-id

.. warning::
   Ne jamais committer le fichier ``.env`` dans Git.
   Ajouter ``.env`` dans ``.gitignore``.

Vérification de l'installation
===============================

Lancer le serveur de développement
-----------------------------------

.. code-block:: bash

   python manage.py runserver

Ouvrir un navigateur et accéder à :

   http://127.0.0.1:8000/

Vous devriez voir la page d'accueil d'OC Lettings.

Vérifier l'interface admin
---------------------------

Accéder à :

   http://127.0.0.1:8000/admin/

Se connecter avec le superutilisateur créé précédemment.

Exécuter les tests
------------------

.. code-block:: bash

   # Exécuter tous les tests
   pytest


Vérifier le linting
-------------------

.. code-block:: bash

   # Vérifier la conformité PEP 8
   flake8

.. note::
   Tous les tests doivent passer et le linting ne doit signaler aucune erreur.


Étapes suivantes
================

Une fois l'installation terminée, consulter :

- :doc:`quickstart` pour un guide de démarrage rapide
- :doc:`usage` pour apprendre à utiliser l'application
- :doc:`deployment` pour déployer en production