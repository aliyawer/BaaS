FROM python:3.8

WORKDIR /app/
COPY . .
RUN pip3 install -r requirements.txt
CMD celery -A app.celery worker --loglevel=info & python3 app.py