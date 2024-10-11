import numpy as np # pragma: no cover

self = type('Mock', (), {'_testRandom': lambda *args: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/where_op_test.py
from l3.Runtime import _l_
self._testRandom(np.int8, None, array_ops.where_v2)
_l_(5075)
