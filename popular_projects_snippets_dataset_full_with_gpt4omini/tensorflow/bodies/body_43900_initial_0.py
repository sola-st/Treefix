import numpy as np # pragma: no cover

iterable = [np.array([1]), np.array([2]), np.array([3])] # pragma: no cover
strat = type('Mock', (object,), {'reduce': staticmethod(lambda operation, arr, axis=0: np.sum(arr, axis=axis))})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_distributed_test.py
from l3.Runtime import _l_
s = 0
_l_(9458)
for pr in iterable:
    _l_(9460)

    # TODO(mdan): It would be nice to be able to write s = s * 10 + pr.
    s = s * 10 + strat.reduce('SUM', pr, axis=0)
    _l_(9459)
aux = s
_l_(9461)
exit(aux)
