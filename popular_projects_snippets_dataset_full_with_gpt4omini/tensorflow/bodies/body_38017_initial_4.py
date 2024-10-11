import numpy as np # pragma: no cover

math_ops = type('Mock', (object,), {'less_equal': np.less_equal})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
from l3.Runtime import _l_
self._testBCastByFunc(np.less_equal, math_ops.less_equal)
_l_(7953)
