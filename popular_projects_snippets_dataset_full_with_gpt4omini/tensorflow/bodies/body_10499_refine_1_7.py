ops = type('MockOps', (object,), {'control_dependencies': lambda x: x})() # pragma: no cover
gen_math_ops = type('MockGenMathOps', (object,), {'tanh_grad': staticmethod(lambda y, g: g * (1 - tf.square(y)))})() # pragma: no cover

class MockOp:  # Mock class to simulate an operation # pragma: no cover
    def __init__(self): # pragma: no cover
        pass
op = MockOp() # pragma: no cover
class MockOps:  # Mock class for ops # pragma: no cover
    @staticmethod # pragma: no cover
    def control_dependencies(deps): # pragma: no cover
        return deps # pragma: no cover
ops = MockOps() # pragma: no cover
  # TensorFlow math module # pragma: no cover
class MockGenMathOps:  # Mock class for general math operations # pragma: no cover
    @staticmethod # pragma: no cover
    def tanh_grad(y, g): # pragma: no cover
        return g * (1 - tf.square(y)) # pragma: no cover
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
