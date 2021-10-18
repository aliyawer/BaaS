FROM python:3.8

WORKDIR /app/
COPY . .
RUN pip3 install -r requirements.txt

RUN apt-get update
RUN apt-get -y upgrade
RUN apt install -y octave
CMD python3 app.py & celery -A app.celery worker --loglevel=info