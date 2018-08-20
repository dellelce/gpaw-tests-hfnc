"""


"""

import json
from pprint import pprint
from auto import execution


def cycle(filename="19.json", start=-1.10, stop=-1.80, step=0.05, atom=1, baselabel='xx'):
    with open(filename) as fh:
        b = fh.read()
        d = json.loads(b)

    status = start

    while status >= stop:
        d['xyz'][atom][2] = status
        pprint(d['xyz'][atom])
        label=str(status).replace('-','')
        label=label.replace('.','_')
        label=label[:6]
        x = execution(d)
        x.run(baselabel+label)
        status -= step




if __name__ == '__main__':
    # initial cycle: start=-1.10, stop=-1.80, step=0.05, atom=1

    cycle(start=-1.80, stop=-2.01, step=0.05, atom=1)
