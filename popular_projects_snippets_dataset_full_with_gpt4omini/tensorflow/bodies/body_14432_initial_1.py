import numpy as np # pragma: no cover

_scalar = lambda func, val, wrap: func(val) if not wrap else -func(-val) # pragma: no cover
class MockMathOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def floor(x):# pragma: no cover
        return np.floor(x)# pragma: no cover
math_ops = MockMathOps() # pragma: no cover
x = 3.7 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
from l3.Runtime import _l_
aux = _scalar(math_ops.floor, x, True)
_l_(6228)
exit(aux)
