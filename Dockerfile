FROM python
RUN pip install pip setuptools -U 

COPY ./requirements.txt /src/requirements.txt
WORKDIR /src
RUN pip install -r requirements.txt

ENTRYPOINT cd src/ && echo 'exec(open("setup.py").read())' | python manage.py shell && uwsgi --socket :8000 --wsgi-file ctf/wsgi.py
