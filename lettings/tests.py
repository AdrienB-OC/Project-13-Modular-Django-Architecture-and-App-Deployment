from django.urls import reverse
from .models import Address, Letting


def test_lettings_index(client):
    url = reverse('lettings_index')
    response = client.get(url)

    assert response.status_code == 200
    assert b'<title>Lettings</title>' in response.content


def test_letting(client):
    address = Address.objects.create(number=340, street='Wintergreen Avenue',
                                     city="Newport News", state="VA",
                                     zip_code="23601", country_iso_code="USA")
    Letting.objects.create(title="'Silo Studio' Cottage", address=address)

    url = reverse('letting', kwargs={'letting_id': 1})
    response = client.get(url)

    assert response.status_code == 200
    assert b"<title>&#x27;Silo Studio&#x27; Cottage</title>" in response.content
