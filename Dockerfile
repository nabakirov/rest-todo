FROM python:3.8-slim

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

CMD python manage.py migrate && gunicorn rest_todo.wsgi --workers 3 --bind unix:/sockets/rest_todo.sock
