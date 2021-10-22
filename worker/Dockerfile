FROM python:3.8

WORKDIR /app/
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y octave
COPY BENCHOP ./BENCHOP
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

CMD celery -A app.celery worker --loglevel=info --broker='amqp://admin:admin@192.168.2.121:5672/'