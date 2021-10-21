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
    res_1 = task_1.delay()
    res_2 = task_2.delay()
    res = {
        "res_1": res_1.get(),
        "res_2": res_2.get(),
    }
    return res

def flatten_list(the_list):
    flattened_list = []
    for sublist in the_list:
        for subsublist in sublist:
            flattened_list.append(subsublist)
    return flattened_list


@celery.task(name="app.task_1")
def task_1():
    oc = Oct2Py()
    oc.addpath('./BENCHOP')
    time, res = oc.Table_1a(nout=2)
    flat_time = flatten_list(time)
    flat_res = flatten_list(res)

    result_dict = {
        "flat_time": flat_time,
        "flat_res": flat_res
    }
    return result_dict

@celery.task(name="app.task_2")
def task_2():
    oc = Oct2Py()
    oc.addpath('./BENCHOP')
    time, res = oc.Table_1b1(nout=2)
    flat_time = flatten_list(time)
    flat_res = flatten_list(res)

    result_dict = {
        "flat_time": flat_time,
        "flat_res": flat_res
    }
    return result_dict


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
