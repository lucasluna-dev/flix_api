from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.renderers import JSONRenderer

from movies.views import MoviesStatsView
from movies.models import Movies
from genres.models import Genre
from reviews.models import Review


def ensure_seed_data():
    with transaction.atomic():
        genre, _ = Genre.objects.get_or_create(name="Sci-Fi")
        movie, _ = Movies.objects.get_or_create(title="Seed Movie", defaults={"genre": genre})
        # Attach genre if created without due to defaults
        if movie.genre_id is None:
            movie.genre = genre
            movie.save(update_fields=["genre"])
        # Create a couple of reviews if none exist
        if not Review.objects.filter(movie=movie).exists():
            Review.objects.create(movie=movie, stars=4)
            Review.objects.create(movie=movie, stars=5)


def get_or_create_superuser():
    User = get_user_model()
    user, created = User.objects.get_or_create(username="admin", defaults={
        "is_staff": True,
        "is_superuser": True,
        "email": "admin@example.com",
    })
    if created:
        user.set_password("admin")
        user.save()
    return user


def run():
    ensure_seed_data()
    user = get_or_create_superuser()

    factory = APIRequestFactory()
    req = factory.get("/api/v1/movies/stats/")
    force_authenticate(req, user=user)

    view = MoviesStatsView.as_view()
    resp = view(req)

    # Render to JSON to ensure serializability
    output = JSONRenderer().render(resp.data)
    print(output.decode("utf-8"))


if __name__ == "__main__":
    run()

