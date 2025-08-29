from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


APPS = ("actors", "genres", "movies", "reviews")
GROUP_NAME = "default_viewer"


class Command(BaseCommand):
    help = (
        "Create or update the 'default_viewer' group with all 'view_*' permissions "
        "for actors, genres, movies and reviews."
    )

    def handle(self, *args, **options):
        group, _ = Group.objects.get_or_create(name=GROUP_NAME)

        view_perms = []
        for app_label in APPS:
            content_types = ContentType.objects.filter(app_label=app_label)
            perms = Permission.objects.filter(content_type__in=content_types, codename__startswith="view_")
            view_perms.extend(list(perms))

        group.permissions.set(list({p.id: p for p in view_perms}.values()))
        group.save()

        self.stdout.write(self.style.SUCCESS(
            f"Group '{GROUP_NAME}' now has {group.permissions.count()} 'view_*' permissions."
        ))

