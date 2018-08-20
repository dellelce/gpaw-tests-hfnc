"""


"""

import json
from pprint import pprint
from auto import execution


def cycle(filename="19.json", start=-1.10, stop=-1.80, step=0.05, atom=1, position=2, baselabel='xx'):
    with open(filename) as fh:
        b = fh.read()
        d = json.loads(b)

    status = start

    while status >= stop:
        d['xyz'][atom][position] = status
        pprint(d['xyz'][atom])
        label=str(status).replace('-','')
        label=label.replace('.','_')
        label=label[:6]
        x = execution(d)
        x.run(baselabel+label)
        status -= step




if __name__ == '__main__':
    # initial cycle: start=-1.10, stop=-1.80, step=0.05, atom=1

    # run 2: cycle(start=-1.80, stop=-2.01, step=0.05, atom=1)
    # run 3 cycle(start=-1.825, stop=-2.01, step=0.05, atom=1)
    # run 4: cycle(start=-1.8125, stop=-2.01, step=0.05, atom=1)

    '''
    up to run 4 the best energy is for HF-N: 1.8125 HF-C: 1.70 
    from run 5 we start moving the carbon
    '''
    # run 5: cycle(start=-1.40, stop=-2.01, step=0.05, atom=2, position=1, baselabel='yy')

    '''
    run 5 moved carbon atom from 1.40 to 1.95, but 1.95 did not converge
    Nitrogen stayed fixed at 1.45
    Best energy for Hf-C at 1.90
    '''
    cycle(start=-1.40, stop=-2.01, step=0.05, atom=2, position=1, baselabel='yy')
