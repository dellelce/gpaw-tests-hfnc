"""


"""

import json
from pprint import pprint
from auto import execution


def cycle(filename="19.json", start=-1.10, stop=-1.80, step=0.05):
    with open(filename) as fh:
        b = fh.read()
        d = json.loads(b)

    status = start

    while status >= stop:
        d['xyz'][1][2] = status
        pprint(d['xyz'][1])
        label=str(status).replace('-','')
        label=label.replace('.','_')
        x = execution(d)
        x.run('xx'+label)
        status -= step




if __name__ == '__main__':
    cycle()
