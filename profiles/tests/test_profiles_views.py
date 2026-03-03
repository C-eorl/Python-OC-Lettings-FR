import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_index_view(client):
    # Crée quelques profils
    user1 = User.objects.create_user(username="user1", password="1234")
    user2 = User.objects.create_user(username="user2", password="1234")
    Profile.objects.create(user=user1, favorite_city="Paris")
    Profile.objects.create(user=user2, favorite_city="Lyon")

    url = reverse("profiles:index")
    response = client.get(url)

    assert response.status_code == 200
    assert "profiles_list" in response.context
    assert len(response.context["profiles_list"]) == 2


@pytest.mark.django_db
def test_profiles_profile_detail_view(client):
    user = User.objects.create_user(username="testuser", password="1234")
    profile = Profile.objects.create(user=user, favorite_city="Paris")

    url = reverse("profiles:profile", args=[user.username])
    response = client.get(url)

    assert response.status_code == 200
    assert response.context["profile"] == profile


@pytest.mark.django_db
def test_profiles_profile_404(client):
    url = reverse("profiles:profile", args=["unknownuser"])
    response = client.get(url)
    assert response.status_code == 404
