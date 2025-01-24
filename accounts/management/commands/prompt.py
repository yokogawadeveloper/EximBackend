import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Read and display a file content'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the file to read')

    def handle(self, *args, **options):
        file_path = options['file_path']

        if not os.path.isfile(file_path):
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
            return

        with open(file_path, 'r') as file:
            content = file.read()

        self.stdout.write(self.style.SUCCESS(f'File content:\n{content}'))
