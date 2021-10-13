#!flask/bin/python
from flask import Flask
from celery import Celery

app = Flask(__name__)

celery = Celery('worker',
                broker="amqp://admin:admin@rabbit",
                backend="rpc://")

@app.route('/baas', methods=['GET'])
def baas_project():
    result = benchop.delay()
    return result.get()


@celery.task(name="app.benchop")
def benchop():
    return "Benchop task is running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
