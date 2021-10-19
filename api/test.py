from oct2py import octave
from oct2py import Oct2Py


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


result = benchop()
print(result)
