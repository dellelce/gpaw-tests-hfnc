"""


"""

import json
from pprint import pprint
from auto import execution


def cycle(filename="19.json", start=-1.10, stop=-1.80, step=0.05, atom=1, position=2, baselabel='xx'):
    cnt = 0
    with open(filename) as fh:
        b = fh.read()
        d = json.loads(b)

    status = start

    while status >= stop:
        d['xyz'][atom][position] = status
        pprint(d['xyz'])
        label=str(status).replace('-','')
        label=label.replace('.','_')
        label=label[:6]
        print("this step: {}".format(status))
        x = execution(d)
        x.run(baselabel+label)
        cnt += 1
        status = step

    print("cycle() completed with {} executions.".format(cnt))


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
    Run 6 will move C with from 1.805 to 1.94 with step 0.025 and keep N at 1.8125
    Run 6 did not converge at 1.8549 and the best execution was at 1.8299
    Hence best lengths with these calculations are: Hf-N: 1.8125 and HF-C: 1.8299 which are also
    very close to non-convergence lengths
    '''
    #cycle(filename="19.r6.json", start=-1.805,
    #                             stop=-1.941, step=0.025, atom=2, position=1, baselabel='zz')
    '''
    Run 7 Moves Hf on Z from -0.10 to 0.10
    Original run 7 does not converge
    '''
    #cycle(filename="19.ok0.json", start=0.10,
    #                              stop=-0.10,
    #                              step=-0.01, atom=0, position=2, baselabel='yz')
    #cycle(filename="19.ok1.json", start=0.06,
    #                              stop=-0.06,
    #                              step=-0.01, atom=0, position=2, baselabel='yz')
    # original "Run 7" with correct position (=3)
    cycle(filename="19.ok0-correct.json",
          start=0.10,
          stop=-0.10,
          step=-0.01,
          atom=0,
          position=3,
          baselabel='za')
