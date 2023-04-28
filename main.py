import os
from dotenv import load_dotenv

from django.core.management import execute_from_command_line

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
execute_from_command_line('manage.py runserver 127.0.0.1:8000'.split())
