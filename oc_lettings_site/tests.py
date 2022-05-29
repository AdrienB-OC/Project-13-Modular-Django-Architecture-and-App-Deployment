from django.urls import reverse


def test_index(client):
    url = reverse('index')
    response = client.get(url)

    assert response.status_code == 200
    assert b'<h1>Welcome to Holiday Homes</h1>' in response.content
