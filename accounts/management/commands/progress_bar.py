from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Updates last_login for all users'

    def handle(self, *args, **options):
        users = User.objects.all()
        total = users.count()

        with tqdm(total=total) as progress_bar:
            for user in users:
                user.last_login = timezone.now()
                user.save()
                progress_bar.update(1)

        self.stdout.write(self.style.SUCCESS(f'Updated last_login for {total} users'))