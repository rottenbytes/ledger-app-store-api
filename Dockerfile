FROM debian:buster
RUN apt-get update
RUN apt-get install -y python3 pipenv python3-dev libpq-dev

WORKDIR /app
COPY . /app

EXPOSE 8000

RUN pipenv install
CMD pipenv run python manage.py migrate && pipenv run python manage.py runserver 0.0.0.0:8000