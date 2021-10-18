#!flask/bin/python
from flask import Flask
from celery import Celery
from oct2py import octave
from oct2py import Oct2Py

app = Flask(__name__)

celery = Celery('worker',
                broker="amqp://admin:admin@rabbit:5672//",
                backend="rpc://")


@app.route('/baas', methods=['GET'])
def baas_project():
    result = benchop.delay()
    return result.get()


@celery.task(name="app.benchop")
def benchop():
    oc = Oct2Py()
    oc.addpath(octave.genpath('./BENCHOP'))
    res = oc.Table_1a()
    flat_res = []
    for r in res:
        for el in r:
            flat_res.append(el)

    return flat_res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
