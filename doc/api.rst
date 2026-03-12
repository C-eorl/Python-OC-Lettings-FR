===================================
Interfaces de programmation
===================================

Cette section décrit l'architecture de l'application, les vues disponibles,
et les interfaces de programmation internes.

Architecture de l'application
==============================

OC Lettings suit le pattern **MVT** (Model-View-Template) de Django :

.. code-block:: text

   ┌─────────────┐
   │   Client    │ ──── HTTP Request ───▶
   └─────────────┘
                                         ┌──────────────┐
                                         │   urls.py    │
                                         │   (Routing)  │
                                         └──────────────┘
                                                │
                                                ▼
                                         ┌──────────────┐
                                         │   views.py   │
                                         │  (Logique)   │
                                         └──────────────┘
                                                │
                        ┌───────────────────────┼───────────────────────┐
                        ▼                       ▼                       ▼
                 ┌──────────────┐       ┌──────────────┐       ┌──────────────┐
                 │  models.py   │       │ templates/   │       │   Context    │
                 │ (Base de     │       │  (HTML)      │       │   Data       │
                 │  données)    │       │              │       │              │
                 └──────────────┘       └──────────────┘       └──────────────┘
                        │                       │                       │
                        └───────────────────────┼───────────────────────┘
                                                ▼
                                         ┌──────────────┐
                                         │  Response    │
   ┌─────────────┐                       │    HTML      │
   │   Client    │ ◀──── HTTP Response ──┤              │
   └─────────────┘                       └──────────────┘

Configuration des URLs
======================

Routing principal
-----------------

**Fichier** : ``oc_lettings_site/urls.py``

.. code-block:: python

   from django.urls import path, include
   from . import views

   urlpatterns = [
        path('', views.index, name='index'),
        path('profiles/', include('profiles.urls', namespace='profiles')),
        path('lettings/', include('lettings.urls', namespace='lettings')),
        path('admin/', admin.site.urls),
   ]

Application lettings
--------------------

**Fichier** : ``lettings/urls.py``

.. code-block:: python

   from django.urls import path
   from . import views

   app_name = 'lettings'

   urlpatterns = [
       path('', views.index, name='index'),
       path('<int:letting_id>/', views.letting, name='letting'),
   ]

**Namespace** : ``lettings``

**URLs disponibles** :

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - URL
     - Nom
     - Description
   * - ``/lettings/``
     - ``lettings:index``
     - Liste de toutes les locations
   * - ``/lettings/<id>/``
     - ``lettings:letting``
     - Détail d'une location spécifique

Application profiles
--------------------

**Fichier** : ``profiles/urls.py``

.. code-block:: python

   from django.urls import path
   from . import views

   app_name = 'profiles'

   urlpatterns = [
       path('', views.index, name='index'),
       path('<str:username>/', views.profile, name='profile'),
   ]

**Namespace** : ``profiles``

**URLs disponibles** :

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - URL
     - Nom
     - Description
   * - ``/profiles/``
     - ``profiles:index``
     - Liste de tous les profils
   * - ``/profiles/<username>/``
     - ``profiles:profile``
     - Détail d'un profil utilisateur

Vues (Views)
============

Application principale
----------------------

**Fichier** : ``oc_lettings_site/views.py``

.. py:function:: index(request)

   Affiche la page d'accueil du site OC Lettings.

   :param request: L'objet HttpRequest de Django
   :type request: HttpRequest
   :return: Page HTML d'accueil rendue
   :rtype: HttpResponse

   **Template** : ``templates/index.html``

   **Exemple d'utilisation** :

   .. code-block:: python

      # Dans urls.py
      path('', views.index, name='index')

Application lettings
--------------------

.. py:function:: lettings.views.index(request)

   Affiche la liste de toutes les locations disponibles.

   :param request: L'objet HttpRequest de Django
   :type request: HttpRequest
   :return: Page HTML avec la liste des lettings
   :rtype: HttpResponse

   **Template** : ``lettings/templates/lettings/index.html``

   **Context** :

   .. code-block:: python

      {
          'lettings_list': [<Letting>, <Letting>, ...]
      }

   **Requête ORM** :

   .. code-block:: python

      lettings_list = Letting.objects.all()

.. py:function:: lettings.views.letting(request, letting_id)

   Affiche le détail d'une location spécifique.

   :param request: L'objet HttpRequest de Django
   :type request: HttpRequest
   :param letting_id: ID de la location à afficher
   :type letting_id: int
   :return: Page HTML avec les détails du letting
   :rtype: HttpResponse
   :raises Http404: Si le letting_id n'existe pas

   **Template** : ``lettings/templates/lettings/letting.html``

   **Context** :

   .. code-block:: python

      {
          'title': "Comfortable studio",
          'address': <Address object>
      }

   **Requête ORM** :

   .. code-block:: python

      letting = Letting.objects.get(id=letting_id)

Application profiles
--------------------

.. py:function:: profiles.views.index(request)

   Affiche la liste de tous les profils utilisateurs.

   :param request: L'objet HttpRequest de Django
   :type request: HttpRequest
   :return: Page HTML avec la liste des profils
   :rtype: HttpResponse

   **Template** : ``profiles/templates/profiles/index.html``

   **Context** :

   .. code-block:: python

      {
          'profiles_list': [<Profile>, <Profile>, ...]
      }

   **Requête ORM** :

   .. code-block:: python

      profiles_list = Profile.objects.all()

.. py:function:: profiles.views.profile(request, username)

   Affiche le détail d'un profil utilisateur spécifique.

   :param request: L'objet HttpRequest de Django
   :type request: HttpRequest
   :param username: Nom d'utilisateur du profil
   :type username: str
   :return: Page HTML avec les détails du profil
   :rtype: HttpResponse
   :raises Http404: Si le username n'existe pas

   **Template** : ``profiles/templates/profiles/profile.html``

   **Context** :

   .. code-block:: python

      {
          'profile': <Profile object>
      }

   **Requête ORM** :

   .. code-block:: python

      profile = Profile.objects.get(user__username=username)

Modèles (Models)
================

Référence des modèles détaillée dans :doc:`database`.

Résumé des APIs internes
-------------------------

**lettings.models.Address**

.. code-block:: python

   from lettings.models import Address

   # Créer une adresse
   address = Address.objects.create(
       number=123,
       street="Main St",
       city="Springfield",
       state="IL",
       zip_code=62701,
       country_iso_code="USA"
   )

   # Récupérer toutes les adresses
   addresses = Address.objects.all()

   # Filtrer par ville
   addresses_in_city = Address.objects.filter(city="Springfield")

**lettings.models.Letting**

.. code-block:: python

   from lettings.models import Letting

   # Créer un letting
   letting = Letting.objects.create(
       title="Beautiful apartment",
       address=address
   )

   # Accéder à l'adresse via le letting
   print(letting.address.city)

**profiles.models.Profile**

.. code-block:: python

   from profiles.models import Profile
   from django.contrib.auth.models import User

   # Créer un utilisateur et son profil
   user = User.objects.create_user(
       username='john_doe',
       email='john@example.com',
       password='securepassword123'
   )
   profile = Profile.objects.create(
       user=user,
       favorite_city='Paris'
   )

   # Accéder au profil depuis l'utilisateur
   print(user.profile.favorite_city)

Templates
=========

Structure des templates
-----------------------

.. code-block:: text

   templates/
   ├── base.html                    # Template de base (hérité par tous)
   ├── index.html                   # Page d'accueil
   ├── 404.html                     # Page erreur 404
   └── 500.html                     # Page erreur 500

   profiles/templates/
   └── lettings/
       ├── index.html               # Liste des lettings
       └── letting.html             # Détail d'un letting
   lettings/templates/
   └── profiles/
       ├── index.html               # Liste des profils
       └── profile.html             # Détail d'un profil

Template de base
----------------

**Fichier** : ``templates/base.html``

Contient :

- Barre de navigation
- Inclusions CSS/JS
- Blocs ``{% block title %}`` et ``{% block content %}``

**Exemple d'héritage** :

.. code-block:: html+django

   {% extends 'base.html' %}

   {% block title %}Mon Titre{% endblock %}

   {% block content %}
   <h1>Mon Contenu</h1>
   {% endblock %}

Interface d'administration
===========================

Django Admin est accessible à ``/admin/``

Modèles enregistrés
-------------------

**lettings.admin** :

- Address
- Letting

**profiles.admin** :

- Profile


Gestion des erreurs
===================

Pages d'erreur personnalisées
------------------------------

**404 - Page non trouvée**

Template : ``templates/404.html``

Déclenchée automatiquement quand :

- URL inexistante
- ``get_object_or_404()`` échoue
- ``Model.objects.get()`` lève ``DoesNotExist``

**500 - Erreur serveur**

Template : ``templates/500.html``

Déclenchée en cas d'exception non gérée.

Configuration requise
---------------------

.. code-block:: python

   # settings.py
   DEBUG = False  # En production uniquement
   ALLOWED_HOSTS = ['votre-domaine.com']

Logging et Sentry
-----------------

Configuration du logging :

.. code-block:: python

   # settings.py
   import sentry_sdk

   sentry_sdk.init(
       dsn=os.environ.get('SENTRY_DSN'),
       traces_sample_rate=1.0,
   )

Les erreurs sont automatiquement envoyées à Sentry en production.

Sécurité
========

Mesures de sécurité Django
---------------------------

- **CSRF Protection** : Activée par défaut
- **SQL Injection** : Prévenue par l'ORM Django
- **XSS** : Échappement automatique dans les templates
- **Clickjacking** : Header ``X-Frame-Options`` activé

Variables sensibles
-------------------

Toujours utiliser des variables d'environnement :

.. code-block:: python

   import os

   SECRET_KEY = os.environ.get('SECRET_KEY')
   SENTRY_DSN = os.environ.get('SENTRY_DSN')
   DATABASE_URL = os.environ.get('DATABASE_URL')

Ne **jamais** committer :

- Clés secrètes
- Mots de passe
- Tokens API
- Fichier ``.env``