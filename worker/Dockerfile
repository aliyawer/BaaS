FROM ubuntu

WORKDIR /app/
COPY ./BENCHOP ./BENCHOP
COPY requirements.txt .
RUN apt-get update
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y octave
ARG DEBIAN_FRONTEND=interactive
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
COPY . .

CMD celery -A app.celery worker --loglevel=info