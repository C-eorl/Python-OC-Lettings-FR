from django.urls import reverse, resolve

from profiles.views import index, profile


def test_profiles_index_url():
    url = reverse("profiles:index")
    assert resolve(url).func == index


def test_profiles_profile_url():
    url = reverse("profiles:profile", args=["username"])
    assert resolve(url).func == profile
