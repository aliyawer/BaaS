#!flask/bin/python
from flask import Flask, jsonify
from celery import Celery
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
    oc.addpath('./BENCHOP')
    time, res = oc.Table_1a(nout=2)
    flat_time = []
    for time_list in time:
        for sublist in time_list:
            flat_time.append(sublist)
    flat_res = []
    for r in res:
        for el in r:
            flat_res.append(el)

    result_dict = {
        "flat_time": flat_time,
        "flat_res": flat_res
    }

    return result_dict


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
