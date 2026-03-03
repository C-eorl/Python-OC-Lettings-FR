import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_lettings_site_index(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
