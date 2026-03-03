from django.contrib import admin
from django.urls import path, include

from . import views

#######################################################################
#                      URL - OC_LETTINGS_SITE                         #
#######################################################################

urlpatterns = [
    path('', views.index, name='index'),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('admin/', admin.site.urls),
]
