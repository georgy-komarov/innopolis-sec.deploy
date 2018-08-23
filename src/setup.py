import os
import subprocess
from sys import stdout
from time import sleep

import psycopg2
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from teamboard.models import Profile

print(f'Current path is: {os.path.abspath(".")}')

print('Django settings:')
for attr in ['ALLOWED_HOSTS', 'BASE_DIR', 'PROJECT_DIR', 'STATICFILES_DIRS']:
    print('\t', attr, getattr(settings, attr, 'FAIL!'))

print('\n\nWaiting for database...')
while True:
    try:
        conn = psycopg2.connect(os.environ['DATABASE_URL'].replace('postgres://', 'postgresql://'))
        break
    except psycopg2.Error:
        sleep(5)

print('Starting migrations')
print(subprocess.check_output('python manage.py collectstatic --noinput', shell=True, stderr=stdout).decode())
print(subprocess.check_output('python manage.py makemigrations', shell=True).decode())
print(subprocess.check_output('python manage.py migrate', shell=True).decode())

subprocess.check_output('chmod -R 755 static', shell=True)

print('Performing initial setup (user)...', end=' ')
has_superuser = User.objects.filter(username="su").exists()

if not has_superuser:
    subprocess.check_output('python manage.py createsuperuser --username=su --email=su@ctf.org --noinput', shell=True)
    user = User.objects.get(username="su")
    user.set_password(os.environ["SU_PASS"])
    user.save()
    Profile(user=user).save()
    print('OK!')
else:
    print('SKIP.')

print('Performing initial setup (site)...', end=' ')
site = Site.objects.get(pk=1)

if site.name == 'example.com' or site.domain == 'example.com':
    site.name = os.environ["NAME"]
    site.domain = os.environ["DOMAIN"]
    site.save()
    print('OK!')
else:
    print('SKIP.')

print('\n\nSetup completed!\n\n')
