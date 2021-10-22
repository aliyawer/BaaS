FROM python:3.8

WORKDIR /app/
RUN apt-get update
RUN apt-get -y upgrade
RUN apt install -y octave
COPY BENCHOP ./BENCHOP
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

CMD python3 app.py