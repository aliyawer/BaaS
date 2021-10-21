FROM python:3.8

WORKDIR /app/
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y octave
COPY . .
RUN pip3 install -r requirements.txt
CMD python3 app.py & celery -A app.celery worker --loglevel=info