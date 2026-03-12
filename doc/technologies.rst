=============================
Technologies et langages
=============================

Stack technique principal
=========================

Langage de programmation
------------------------

**Python 3.10+**
   Langage principal utilisé pour le développement backend.

Framework web
-------------

**Django 5.2**
   Framework web Python pour le développement rapide et sécurisé.

Base de données
---------------

**SQLite 3**
   Base de données relationnelle légère utilisée en développement et production
   (pour ce projet de démonstration).

Environnement de développement
===============================

Gestionnaire de paquets
-----------------------

**pip**
   Gestionnaire de paquets Python standard.

Environnement virtuel
---------------------

**venv**
   Module Python pour créer des environnements virtuels isolés.

Outils de qualité de code
==========================

Linting
-------

**flake8**
   Outil de vérification du respect de la PEP 8 et détection d'erreurs.

   Configuration dans ``setup.cfg`` :

   .. code-block:: ini

      [flake8]
      max-line-length = 99
      exclude = */migrations/*,venv

Tests
-----

**pytest**
   Framework de tests unitaires et d'intégration.

**pytest-django**
   Plugin pytest pour Django.

**pytest-cov**
   Plugin de couverture de tests.

DevOps et déploiement
=====================

Conteneurisation
----------------

**Docker**
   Plateforme de conteneurisation pour empaqueter l'application avec ses dépendances.

**Docker Hub**
   Registre d'images Docker pour stocker et distribuer les images de l'application.

CI/CD
-----

**GitHub Actions**
   Plateforme d'intégration continue et déploiement continu.

   Workflow automatisé :

   1. Linting et tests sur chaque push
   2. Build Docker sur la branche ``main``
   3. Déploiement automatique sur Render

Hébergement
-----------

**Render**
   Plateforme cloud pour héberger l'application en production.

Surveillance
------------

**Sentry**
   Service de monitoring et tracking des erreurs en temps réel.

Documentation
-------------

**Sphinx**
   Générateur de documentation pour Python.

**Read the Docs**
   Plateforme d'hébergement de documentation avec build automatique.

**sphinx-rtd-theme**
   Thème Sphinx optimisé pour Read the Docs.

Frontend
========

**HTML5 / CSS3**
   Structure et styles des pages web.

**JavaScript**
   Scripts côté client pour l'interactivité.

**Bootstrap**
   Framework CSS pour un design responsive.

Contrôle de version
===================

**Git**
   Système de contrôle de version distribué.

**GitHub**
   Plateforme d'hébergement de code source avec fonctionnalités CI/CD.

Dépendances Python principales
===============================

Le fichier ``requirements.txt`` contient toutes les dépendances :

.. code-block:: text

    Django==5.2.12
    flake8==7.3.0
    pytest==9.0.2
    pytest-cov==7.0.0
    pytest-django==4.12.0
    sentry-sdk==2.54.0
    Sphinx==8.1.3
    sphinx_rtd_theme==3.1.0
    whitenoise==6.12.0

