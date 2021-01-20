FROM python:3.8-slim

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

CMD python manage.py migrate && gunicorn -w 3 -b 0.0.0.0:80 ntm.wsgi
