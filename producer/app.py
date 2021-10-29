#!flask/bin/python
from celery import Celery
from oct2py import Oct2Py
from flask import Flask


app = Flask(__name__)

celery = Celery('worker',
                broker="amqp://admin:admin@rabbit:5672/vhost",
                backend="rpc://")


@app.route('/baas', methods=['GET'])
def baas_project():
    res_1 = task_1.delay()
    res_2 = task_2.delay()
    res_3 = task_3.delay()
    res_4 = task_4.delay()
    res_5 = task_5.delay()
    res_6 = task_6.delay()
    res = {
        "res_1": res_1.get(),
        "res_2": res_2.get(),
        "res_3": res_3.get(),
        "res_4": res_4.get(),
        "res_5": res_5.get(),
        "res_6": res_6.get()
    }
    return res


def flatten_list(the_list):
    flattened_list = []
    for sublist in the_list:
        for subsublist in sublist:
            flattened_list.append(subsublist)
    return flattened_list

def create_result_dict(time, res):
    flat_time = flatten_list(time)
    flat_res = flatten_list(res)
    result_dict = {
        "flat_time": flat_time,
        "flat_res": flat_res
    }
    return result_dict


@celery.task(name="app.task_1a1")
def task_1():
    oc = Oct2Py()
    oc.addpath('./BENCHOP')
    time, res = oc.Table_1a1(nout=2)
    return create_result_dict(time,res)


@celery.task(name="app.task_1b1")
def task_2():
    oc = Oct2Py()
    oc.addpath('./BENCHOP')
    time, res = oc.Table_1b1(nout=2)
    return create_result_dict(time,res)

@celery.task(name="app.task_1c1")
def task_3():
    oc = Oct2Py()
    oc.addpath('./BENCHOP')
    time, res = oc.Table_1c1(nout=2)
    return create_result_dict(time,res)

@celery.task(name="app.task_1a2")
def task_4():
    oc = Oct2Py()
    oc.addpath('./BENCHOP')
    time, res = oc.Table_1a2(nout=2)
    return create_result_dict(time,res)

@celery.task(name="app.task_1b2")
def task_5():
    oc = Oct2Py()
    oc.addpath('./BENCHOP')
    time, res = oc.Table_1b2(nout=2)
    return create_result_dict(time,res)

@celery.task(name="app.task_1c2")
def task_6():
    oc = Oct2Py()
    oc.addpath('./BENCHOP')
    time, res = oc.Table_1c2(nout=2)
    return create_result_dict(time,res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
