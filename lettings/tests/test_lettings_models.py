import pytest

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_str():
    address = Address.objects.create(
        number=10,
        street="Main Street",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA"
    )
    assert str(address) == "10 Main Street"


@pytest.mark.django_db
def test_letting_str():
    address = Address.objects.create(
        number=10,
        street="Main Street",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA"
    )
    letting = Letting.objects.create(
        title="Test Letting",
        address=address
    )
    assert str(letting) == "Test Letting"
