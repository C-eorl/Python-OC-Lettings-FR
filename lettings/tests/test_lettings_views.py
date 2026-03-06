import pytest
from django.urls import reverse

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_lettings_index_view(client):
    response = client.get(reverse("lettings:index"))
    assert response.status_code == 200
    assert "lettings_list" in response.context


@pytest.mark.django_db
def test_letting_detail_view(client):
    address = Address.objects.create(
        number=1,
        street="Test Street",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA"
    )
    letting = Letting.objects.create(
        title="My Letting",
        address=address
    )

    response = client.get(reverse("lettings:letting", args=[letting.id]))

    assert response.status_code == 200
    assert response.context["title"] == "My Letting"
    assert response.context["address"] == address


@pytest.mark.django_db
def test_letting_detail_view_invalid(client):

    response = client.get(reverse("lettings:letting", args=[55]))

    assert response.status_code == 404
