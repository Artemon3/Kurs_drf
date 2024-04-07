from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='levkin_mizuno@mail.ru',
            first_name='Artem',
            last_name='Levkin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('bangrang0')
        user.save()