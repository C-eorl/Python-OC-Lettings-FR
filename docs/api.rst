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
