# Create your tests here.
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from hits.models import Artist, Hit

@pytest.mark.django_db
def test_create_hit():
    artist = Artist.objects.create(first_name="Test Artist", last_name="Artist")
    client = APIClient()
    response = client.post(
        reverse("hit-list-create"),
        data={"artist": artist.id, "title": "Nowy Hit"},
        format="json"
    )
    assert response.status_code == 201
    assert Hit.objects.count() == 1


@pytest.mark.django_db
def test_get_hits_list():
    artist = Artist.objects.create(first_name="Test Artist", last_name="Artist")
    for i in range(3):
        Hit.objects.create(title=f"Hit {i}", artist=artist)

    client = APIClient()
    response = client.get(reverse("hit-list-create"))

    assert response.status_code == 200
    assert len(response.data) == 3


@pytest.mark.django_db
def test_get_single_hit():
    artist = Artist.objects.create(first_name="Test Artist", last_name="Artist")
    title = "Super Hit"
    title_url = title.lower().replace(" ", "-")
    hit = Hit.objects.create(title=title, artist=artist, title_url=title_url)

    client = APIClient()
    response = client.get(reverse("hit-detail", kwargs={"title_url": hit.title_url}))

    assert response.status_code == 200
    assert response.data["title"] == title


@pytest.mark.django_db
def test_update_hit():
    artist = Artist.objects.create(first_name="Test Artist", last_name="Artist")
    new_artist = Artist.objects.create(first_name="Test Artist", last_name="Artist")
    hit = Hit.objects.create(title="Old Title", artist=artist, title_url="old-title")

    client = APIClient()
    response = client.put(
        reverse("hit-detail", kwargs={"title_url": hit.title_url}),
        data={"artist": new_artist.id, "title": "New Title"},
        format="json"
    )

    assert response.status_code == 200
    hit.refresh_from_db()
    assert hit.title == "New Title"
    assert hit.artist == new_artist

@pytest.mark.django_db
def test_delete_hit():
    artist = Artist.objects.create(first_name="Test Artist", last_name="Artist")
    hit = Hit.objects.create(title="To Be Deleted", artist=artist, title_url="to-be-deleted")

    client = APIClient()
    response = client.delete(reverse("hit-detail", kwargs={"title_url": hit.title_url}))

    assert response.status_code == 204
    assert Hit.objects.count() == 0
