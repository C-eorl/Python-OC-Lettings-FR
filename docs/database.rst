===================================
Structure de la base de données
===================================

Architecture de la base de données
===================================

OC Lettings utilise **SQLite 3** comme système de gestion de base de données.
La structure est organisée en trois applications Django distinctes.

Schéma relationnel
==================

Diagramme ER simplifié
----------------------

.. code-block:: text

   ┌──────────────────┐
   │   auth_user      │
   │──────────────────│
   │ id (PK)          │
   │ username         │
   │ first_name       │
   │ last_name        │
   │ email            │
   │ password         │
   └──────────────────┘
            │
            │ 1:1
            ▼
   ┌──────────────────┐
   │  profiles_profile│
   │──────────────────│
   │ id (PK)          │
   │ user_id (FK)     │
   │ favorite_city    │
   └──────────────────┘


   ┌──────────────────┐
   │lettings_address  │
   │──────────────────│
   │ id (PK)          │
   │ number           │
   │ street           │
   │ city             │
   │ state            │
   │ zip_code         │
   │ country_iso_code │
   └──────────────────┘
            │
            │ 1:1
            ▼
   ┌──────────────────┐
   │ lettings_letting │
   │──────────────────│
   │ id (PK)          │
   │ title            │
   │ address_id (FK)  │
   └──────────────────┘

Modèles de données
==================

Application : lettings
----------------------

Address
~~~~~~~

Représente une adresse physique d'un bien immobilier.

**Table** : ``lettings_address``

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Champ
     - Type
     - Description
   * - ``id``
     - Integer (PK)
     - Identifiant unique auto-généré
   * - ``number``
     - PositiveInteger
     - Numéro de rue (1-9999)
   * - ``street``
     - CharField(64)
     - Nom de la rue
   * - ``city``
     - CharField(64)
     - Ville
   * - ``state``
     - CharField(2)
     - Code état US (2 lettres, ex: CA)
   * - ``zip_code``
     - PositiveInteger
     - Code postal US (jusqu'à 99999)
   * - ``country_iso_code``
     - CharField(3)
     - Code pays ISO-3 (ex: USA)


**Exemple de données** :

.. code-block:: python

   {
       "id": 1,
       "number": 7217,
       "street": "Bedford Street",
       "city": "Brunswick",
       "state": "GA",
       "zip_code": 31525,
       "country_iso_code": "USA"
   }

Letting
~~~~~~~

Représente une annonce de location associée à une adresse.

**Table** : ``lettings_letting``

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Champ
     - Type
     - Description
   * - ``id``
     - Integer (PK)
     - Identifiant unique auto-généré
   * - ``title``
     - CharField(256)
     - Titre de l'annonce
   * - ``address_id``
     - ForeignKey (1:1)
     - Référence vers Address

**Relations** :

- Relation **OneToOne** avec ``Address``
- Suppression en cascade : si l'adresse est supprimée, le letting est supprimé

**Exemple de données** :

.. code-block:: python

   {
       "id": 1,
       "title": "Comfortable studio",
       "address": {
           "number": 7217,
           "street": "Bedford Street",
           "city": "Brunswick",
           "state": "GA"
       }
   }

Application : profiles
----------------------

Profile
~~~~~~~

Étend le modèle User de Django avec des informations supplémentaires.

**Table** : ``profiles_profile``

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Champ
     - Type
     - Description
   * - ``id``
     - Integer (PK)
     - Identifiant unique auto-généré
   * - ``user_id``
     - ForeignKey (1:1)
     - Référence vers auth_user
   * - ``favorite_city``
     - CharField(64)
     - Ville favorite (optionnel)

**Relations** :

- Relation **OneToOne** avec ``django.contrib.auth.models.User``
- Suppression en cascade : si l'utilisateur est supprimé, le profil est supprimé

**Exemple de données** :

.. code-block:: python

   {
       "id": 1,
       "user": {
           "username": "john_doe",
           "first_name": "John",
           "last_name": "Doe",
           "email": "john@example.com"
       },
       "favorite_city": "Buenos Aires"
   }

Modèle User (Django)
--------------------

**Table** : ``auth_user``

Modèle standard de Django pour l'authentification.

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Champ
     - Type
     - Description
   * - ``id``
     - Integer (PK)
     - Identifiant unique
   * - ``username``
     - CharField(150)
     - Nom d'utilisateur unique
   * - ``first_name``
     - CharField(150)
     - Prénom
   * - ``last_name``
     - CharField(150)
     - Nom de famille
   * - ``email``
     - EmailField
     - Adresse email
   * - ``password``
     - CharField(128)
     - Mot de passe hashé
   * - ``is_staff``
     - Boolean
     - Accès admin
   * - ``is_active``
     - Boolean
     - Compte actif
   * - ``date_joined``
     - DateTime
     - Date de création

Migrations
==========

Historique des migrations
--------------------------

Application lettings
~~~~~~~~~~~~~~~~~~~~

``0001_initial.py``
   Création des tables ``Address`` et ``Letting``.


Application profiles
~~~~~~~~~~~~~~~~~~~~

``0001_initial.py``
   Création de la table ``Profile``.


Application oc_lettings_site
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``0001_initial.py``
   Tables initiales (architecture monolithique v1.0).

``0002_delete_old_models.py``
   Suppression des anciens models et mise en relation des nouveaux modèles avec les anciennes tables après migration vers architecture modulaire.

