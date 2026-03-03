from django.urls import reverse, resolve

from lettings.views import index, letting


def test_index_url():
    url = reverse("lettings:index")
    assert resolve(url).func == index


def test_letting_url():
    url = reverse("lettings:letting", args=[1])
    assert resolve(url).func == letting
