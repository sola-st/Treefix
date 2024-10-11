import numpy as np # pragma: no cover

x = (4, 16) # pragma: no cover
np = type('Mock', (object,), {'sqrt': staticmethod(lambda y: y ** 0.5)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
from l3.Runtime import _l_
aux = x[0] / np.sqrt(x[1]) if isinstance(x, tuple) else x
_l_(9207)
exit(aux)
