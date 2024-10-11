import numpy as np # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = Mock() # pragma: no cover
class Zeros:# pragma: no cover
    def __call__(self):# pragma: no cover
        return np.zeros((1,)) # pragma: no cover
init_ops_v2 = Mock(Zeros=Zeros) # pragma: no cover
self._range_test = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
from l3.Runtime import _l_
self._range_test(
    init_ops_v2.Zeros(), shape=(4, 5), target_mean=0., target_max=0.)
_l_(22462)
