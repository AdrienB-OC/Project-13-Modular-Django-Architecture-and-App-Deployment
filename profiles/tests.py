from django.urls import reverse
from .models import Profile
from django.contrib.auth.models import User


def test_index(client):
    url = reverse('profiles_index')
    response = client.get(url)
    assert b'<h1>Profiles</h1>' in response.content


def test_profile(client):
    user = User.objects.create(username='HeadlinesGazer', password="test")
    Profile.objects.create(user=user, favorite_city='Buenos Aires')

    url = reverse('profile', kwargs={'username': 'HeadlinesGazer'})
    response = client.get(url)

    assert response.status_code == 200
    assert b'<h1>HeadlinesGazer</h1>' in response.content
