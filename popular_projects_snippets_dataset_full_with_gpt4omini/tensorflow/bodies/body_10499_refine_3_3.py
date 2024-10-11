import numpy as np # pragma: no cover

ops = type('MockOps', (object,), {'control_dependencies': lambda deps: deps})() # pragma: no cover

import numpy as np # pragma: no cover

class MockOp:# pragma: no cover
    pass
op = MockOp() # pragma: no cover
class MockOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def control_dependencies(deps): return deps # pragma: no cover
ops = MockOps() # pragma: no cover
class MockGenMathOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def tanh_grad(y, g): return g * (1 - tf.square(y)) # pragma: no cover
gen_math_ops = MockGenMathOps() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
from l3.Runtime import _l_
"""Returns grad * (1 - tanh(x) * tanh(x))."""
y = op.outputs[0]  # y = tanh(x)
_l_(9600)  # y = tanh(x)
with ops.control_dependencies([grad]):
    _l_(9603)

    y = math_ops.conj(y)
    _l_(9601)
    aux = gen_math_ops.tanh_grad(y, grad)
    _l_(9602)
    exit(aux)
