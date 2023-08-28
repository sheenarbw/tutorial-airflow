from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from dogs.models import Dog

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(10):
            Dog.objects.get_or_create(
                name=f"Dog{i}",
                breed=f"Breed{i}",
                age=i,
                description=f"Description{i}",
            )

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@email.com", "admin")
