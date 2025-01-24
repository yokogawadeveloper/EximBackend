import os
from django.core.management.base import BaseCommand
from accounts.models import User


# class Command(BaseCommand):
#     help = 'Read and display a file content'
#
#     def add_arguments(self, parser):
#         parser.add_argument('file_path', type=str, help='Path to the file to read')
#
#     def handle(self, *args, **options):
#         file_path = options['file_path']
#
#         if not os.path.isfile(file_path):
#             self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
#             return
#
#         with open(file_path, 'r') as file:
#             content = file.read()
#
#         self.stdout.write(self.style.SUCCESS(f'File content:\n{content}'))


# your_app/management/commands/list_books.py
class Command(BaseCommand):
    help = 'List all books in the database'

    def handle(self, *args, **options):
        users = User.objects.all()

        if not users:
            self.stdout.write(self.style.WARNING('No User found.'))
            return

        for user in users:
            self.stdout.write(self.style.SUCCESS(f'User: {user.email} + " " + {user.username}'))
