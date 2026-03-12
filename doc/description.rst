====================
Description du projet
====================

Vue d'ensemble
==============

**OC Lettings** est une application web développée en Django qui permet de gérer
des annonces de locations immobilières et des profils utilisateurs.

L'application offre les fonctionnalités suivantes :

- Consultation des annonces de location disponibles
- Affichage détaillé de chaque bien immobilier avec adresse complète
- Gestion des profils utilisateurs avec ville favorite
- Interface d'administration Django pour la gestion des données
- Architecture modulaire avec séparation des préoccupations

Contexte du projet
==================

Orange County Lettings est une start-up américaine en phase d'expansion dans
le secteur de la location immobilière. L'entreprise a lancé ce projet pour
moderniser son infrastructure technique et améliorer la qualité du code.

Objectifs de la version 2.0
============================

Cette version 2.0 apporte les améliorations suivantes :

**Architecture**
   Refonte complète de l'architecture monolithique vers une structure modulaire
   avec des applications Django distinctes (``lettings``, ``profiles``).

**Qualité du code**
   - Correction de toutes les erreurs de linting
   - Ajout de docstrings complètes sur tous les modules
   - Tests unitaires et d'intégration avec couverture > 80%
   - Gestion des erreurs 404 et 500 personnalisées

**DevOps**
   - Pipeline CI/CD complet avec GitHub Actions
   - Conteneurisation Docker
   - Déploiement automatique sur Render
   - Surveillance des erreurs avec Sentry

**Documentation**
   - Documentation technique complète avec Sphinx
   - Hébergement sur Read the Docs
   - Guides d'installation et de déploiement

Technologies utilisées
======================

Voir la section :doc:`technologies` pour la liste complète des technologies
et frameworks utilisés.

Responsables du projet
======================

- **Directeur Technique** : Dominique
- **Équipe de développement** : Orange County Lettings Team