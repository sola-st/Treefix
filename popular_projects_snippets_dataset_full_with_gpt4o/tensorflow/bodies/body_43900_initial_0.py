import numpy as np # pragma: no cover

iterable = [1, 2, 3, 4] # pragma: no cover
strat = type('Mock', (object,), {'reduce': lambda self, method, pr, axis: pr})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_distributed_test.py
from l3.Runtime import _l_
s = 0
_l_(21811)
for pr in iterable:
    _l_(21813)

    # TODO(mdan): It would be nice to be able to write s = s * 10 + pr.
    s = s * 10 + strat.reduce('SUM', pr, axis=0)
    _l_(21812)
aux = s
_l_(21814)
exit(aux)
