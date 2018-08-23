# innopolis-sec.deploy
### Local deployment (dev server)
```
git clone https://github.com/georgy-komarov/innopolis-sec.deploy.git

cd src/
virtualenv -p python3 ../.env
source ../.env/bin/activate
pip install pip setuptools -U
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username=su --email=su@ctf.org --noinput
echo 'from django.contrib.auth.models import User; from teamboard.models import Profile; user=User.objects.get(username="su"); user.set_password("pass"); user.save(); Profile(user=user).save(); exit(0)' | python manage.py shell
python manage.py runserver 0.0.0.0:8000 -v3 --traceback
```
You can now login with user `su` and password `pass`

### Docker compose
* You must set environment variables in **docker-compose.yml**
* Configure email backend in `src/ctf/settings_docker.py`

Then run `docker-compose up --build`
