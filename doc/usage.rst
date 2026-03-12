==================
Guide d'utilisation
==================

Ce guide présente toutes les fonctionnalités d'OC Lettings avec des cas
d'utilisation concrets.

Interface publique
==================

Page d'accueil
--------------

**URL** : http://127.0.0.1:8000/

La page d'accueil présente deux liens principaux :

- **Lettings** : Accéder à la liste des locations
- **Profiles** : Accéder à la liste des profils

.. image:: https://via.placeholder.com/800x400?text=Homepage+Screenshot
   :alt: Page d'accueil OC Lettings
   :align: center

Navigation des locations
========================

Liste des locations
-------------------

**URL** : http://127.0.0.1:8000/lettings/

Cette page affiche toutes les locations disponibles sous forme de liste.

**Fonctionnalités** :

- Chaque location est cliquable
- Le titre de chaque annonce est affiché
- Lien "Home" pour revenir à l'accueil

**Cas d'utilisation** :

1. Consulter rapidement toutes les locations disponibles
2. Parcourir les titres pour trouver une location intéressante
3. Cliquer sur un titre pour voir les détails

Détail d'une location
---------------------

**URL** : http://127.0.0.1:8000/lettings/<id>/

Exemple : http://127.0.0.1:8000/lettings/1/

**Informations affichées** :

- Titre de la location
- Numéro et nom de rue
- Ville, État et code postal
- Code pays ISO

**Actions disponibles** :

- Bouton "Back" pour revenir à la liste des lettings

**Exemple de données affichées** :

.. code-block:: text

   Comfortable studio

   7217 Bedford Street
   Brunswick, GA 31525
   USA

Navigation des profils
======================

Liste des profils
-----------------

**URL** : http://127.0.0.1:8000/profiles/

Cette page affiche tous les profils utilisateurs.

**Fonctionnalités** :

- Liste de tous les usernames
- Chaque username est cliquable
- Lien "Home" pour revenir à l'accueil

**Cas d'utilisation** :

1. Découvrir les utilisateurs de la plateforme
2. Cliquer sur un username pour voir le profil complet

Détail d'un profil
------------------

**URL** : http://127.0.0.1:8000/profiles/<username>/

Exemple : http://127.0.0.1:8000/profiles/john_doe/

**Informations affichées** :

- Username
- Prénom (First name)
- Nom de famille (Last name)
- Email
- Ville favorite

**Actions disponibles** :

- Bouton "Back" pour revenir à la liste des profils

**Exemple de données affichées** :

.. code-block:: text

   john_doe

   First name: John
   Last name: Doe
   Email: john@example.com
   Favorite city: Buenos Aires

Interface d'administration
==========================

Accès à l'admin Django
----------------------

**URL** : http://127.0.0.1:8000/admin/

**Prérequis** : Avoir créé un superutilisateur

.. code-block:: bash

   python manage.py createsuperuser

Gestion des adresses
---------------------

**Section** : Lettings → Addresses

**Actions disponibles** :

1. **Créer une nouvelle adresse**

   - Cliquer sur "Add Address"
   - Remplir les champs :

     - Number (ex: 123)
     - Street (ex: Main Street)
     - City (ex: Los Angeles)
     - State (ex: CA - 2 lettres obligatoires)
     - Zip code (ex: 90001)
     - Country ISO code (ex: USA - 3 lettres)

   - Cliquer sur "Save"

2. **Modifier une adresse existante**

   - Cliquer sur l'adresse dans la liste
   - Modifier les champs nécessaires
   - Cliquer sur "Save"

3. **Supprimer une adresse**

   - Sélectionner une ou plusieurs adresses
   - Dans le menu "Action", choisir "Delete selected addresses"
   - Confirmer la suppression

   .. warning::
      Supprimer une adresse supprime aussi le letting associé (cascade)

**Recherche et filtres** :

- Rechercher par ville ou état
- Filtrer par état (si configuré dans admin.py)

Gestion des lettings
--------------------

**Section** : Lettings → Lettings

**Actions disponibles** :

1. **Créer un nouveau letting**

   - Cliquer sur "Add Letting"
   - Remplir les champs :

     - Title (ex: Beautiful apartment in downtown)
     - Address (sélectionner une adresse existante)

   - Cliquer sur "Save"

2. **Modifier un letting existant**

   - Cliquer sur le letting dans la liste
   - Modifier le titre ou changer l'adresse
   - Cliquer sur "Save"

3. **Supprimer un letting**

   - Sélectionner un ou plusieurs lettings
   - Action → "Delete selected lettings"
   - Confirmer

**Contraintes** :

- Une adresse ne peut être associée qu'à un seul letting (OneToOne)
- Impossible de créer deux lettings avec la même adresse

Gestion des profils
-------------------

**Section** : Profiles → Profiles

**Actions disponibles** :

1. **Créer un nouveau profil**

   - D'abord créer un utilisateur dans "Users"
   - Puis créer le profil associé :

     - User (sélectionner l'utilisateur)
     - Favorite city (optionnel, ex: Paris)

   - Cliquer sur "Save"

2. **Modifier un profil**

   - Cliquer sur le profil
   - Modifier la ville favorite
   - Cliquer sur "Save"

3. **Supprimer un profil**

   - Sélectionner le(s) profil(s)
   - Action → "Delete selected profiles"
   - Confirmer

   .. note::
      Supprimer l'utilisateur associé supprime aussi le profil (cascade)

Gestion des utilisateurs
-------------------------

**Section** : Authentication and Authorization → Users

Fonctionnalités standard de Django :

- Créer des utilisateurs
- Modifier les permissions
- Activer/désactiver des comptes
- Réinitialiser les mots de passe

Cas d'utilisation pratiques
============================

Cas 1 : Ajouter une nouvelle location
--------------------------------------

**Scénario** : Vous voulez ajouter un nouveau bien à louer.

**Étapes** :

1. Se connecter à l'admin : ``/admin/``
2. Créer l'adresse :

   - Aller dans "Addresses" → "Add Address"
   - Remplir tous les champs
   - Sauvegarder

3. Créer le letting :

   - Aller dans "Lettings" → "Add Letting"
   - Titre : "Cozy 2-bedroom apartment"
   - Adresse : Sélectionner l'adresse créée
   - Sauvegarder

4. Vérifier sur le site public :

   - Aller sur ``/lettings/``
   - Le nouveau letting apparaît dans la liste

Cas 2 : Ajouter un nouveau membre
----------------------------------

**Scénario** : Un nouvel utilisateur s'inscrit sur la plateforme.

**Étapes** :

1. Créer l'utilisateur :

   - Admin → "Users" → "Add User"
   - Username : "alice_smith"
   - Password : (mot de passe sécurisé)
   - Sauvegarder

2. Compléter les informations :

   - First name : Alice
   - Last name : Smith
   - Email : alice@example.com
   - Sauvegarder

3. Créer le profil :

   - Admin → "Profiles" → "Add Profile"
   - User : alice_smith
   - Favorite city : Tokyo
   - Sauvegarder

4. Vérifier :

   - Aller sur ``/profiles/``
   - Le profil "alice_smith" apparaît

Cas 3 : Modifier une adresse
-----------------------------

**Scénario** : Une adresse a changé (nouveau code postal, par exemple).

**Étapes** :

1. Admin → "Addresses"
2. Trouver l'adresse via la recherche ou la liste
3. Cliquer sur l'adresse
4. Modifier le champ "Zip code"
5. Sauvegarder
6. Le changement est immédiatement visible sur ``/lettings/<id>/``

Cas 4 : Supprimer un letting obsolète
--------------------------------------

**Scénario** : Une location n'est plus disponible.

**Étapes** :

1. Admin → "Lettings"
2. Cocher la case du letting à supprimer
3. Action → "Delete selected lettings"
4. Confirmer la suppression

.. note::
   L'adresse associée n'est PAS supprimée, uniquement le letting.
   Pour supprimer aussi l'adresse, aller dans "Addresses" et la supprimer.

Cas 5 : Rechercher un profil
-----------------------------

**Scénario** : Trouver rapidement le profil d'un utilisateur.

**Méthode 1 - Via l'admin** :

1. Admin → "Profiles"
2. Utiliser la barre de recherche
3. Entrer le username ou la ville favorite

**Méthode 2 - Via l'interface publique** :

1. Aller sur ``/profiles/``
2. Parcourir la liste des usernames
3. Cliquer sur le username souhaité

Bonnes pratiques d'utilisation
===============================

Validation des données
----------------------

**Adresses** :

- Le state doit faire exactement 2 caractères (ex: CA, NY)
- Le country_iso_code doit faire exactement 3 caractères (ex: USA, FRA)
- Le zip_code doit être inférieur à 99999
- Le number doit être inférieur à 9999

**Profils** :

- Le username doit être unique
- La ville favorite est optionnelle

Suppression sécurisée
---------------------

.. warning::
   Avant de supprimer des données :

   1. Vérifier les dépendances (relations OneToOne)
   2. Faire une sauvegarde si nécessaire
   3. Confirmer que les données ne sont plus nécessaires

**Relations de suppression en cascade** :

- Supprimer une **adresse** → supprime le **letting** associé
- Supprimer un **utilisateur** → supprime le **profil** associé

