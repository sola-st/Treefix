import sys # pragma: no cover
import math # pragma: no cover

x = 10 # pragma: no cover
_scalar = lambda func, arg, flag: func(arg) if flag else arg # pragma: no cover
math_ops = type('Mock', (object,), {'floor': math.floor})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
from l3.Runtime import _l_
aux = _scalar(math_ops.floor, x, True)
_l_(18510)
exit(aux)
