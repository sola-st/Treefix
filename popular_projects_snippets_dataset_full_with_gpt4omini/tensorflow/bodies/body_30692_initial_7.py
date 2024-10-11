import numpy as np # pragma: no cover

class Mock: # pragma: no cover
    def _testRandom(self, dtype, arg1, arg2): pass# pragma: no cover
self = Mock() # pragma: no cover
array_ops = type('MockArrayOps', (object,), {'where_v2': lambda condition, x, y: x if condition else y})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/where_op_test.py
from l3.Runtime import _l_
self._testRandom(np.int8, None, array_ops.where_v2)
_l_(5075)
