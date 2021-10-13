#!flask/bin/python
from flask import Flask
from celery import Celery
from oct2py import octave

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
    oc = Oct2Py()
    oc.addpath(octave.genpath('./BENCHOP'))
    time, res = oc.Table_1a()
    print("Calling Benchop")
    return (time, res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
