class Mock: # pragma: no cover
    def _range_test(self, init_op, shape, target_mean, target_max): # pragma: no cover
        pass # pragma: no cover
self = Mock() # pragma: no cover
class InitOpsV2: # pragma: no cover
    def Zeros(self): # pragma: no cover
        return [[0 for _ in range(5)] for _ in range(4)] # pragma: no cover
init_ops_v2 = InitOpsV2() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
from l3.Runtime import _l_
self._range_test(
    init_ops_v2.Zeros(), shape=(4, 5), target_mean=0., target_max=0.)
_l_(10269)
