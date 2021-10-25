FROM python:3.8

WORKDIR /app/
COPY BENCHOP ./BENCHOP
COPY requirements.txt .
RUN apt-get update
RUN apt-get install -y octave
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .

CMD python3 app.py