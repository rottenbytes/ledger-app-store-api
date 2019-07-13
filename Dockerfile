FROM debian:buster
RUN apt-get update
RUN apt-get install -y python3 pipenv python3-dev default-libmysqlclient-dev libpq-dev 

WORKDIR /app
COPY . /app

RUN pipenv install
CMD pipenv run python manage.py runserver
