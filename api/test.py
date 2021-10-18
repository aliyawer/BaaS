from oct2py import octave
from oct2py import Oct2Py


def benchop():
    oc = Oct2Py()
    oc.addpath(octave.genpath('./BENCHOP'))
    res = oc.Table_1a()
    flat_res = []
    for r in res:
        for el in r:
            flat_res.append(el)

    return flat_res


res = benchop()
print(res)
