import numpy as np # pragma: no cover

self = type('Mock', (object,), {'_testBCastByFunc': lambda self, a, b: None})() # pragma: no cover
np = type('Mock', (object,), {'less_equal': None})() # pragma: no cover
math_ops = type('Mock', (object,), {'less_equal': None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
from l3.Runtime import _l_
self._testBCastByFunc(np.less_equal, math_ops.less_equal)
_l_(20610)
