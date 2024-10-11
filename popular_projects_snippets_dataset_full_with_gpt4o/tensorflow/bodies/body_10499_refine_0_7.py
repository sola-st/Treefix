ops = type('Mock', (object,), {'control_dependencies': lambda x: tf.control_dependencies(x)}) # pragma: no cover

ops = type('Mock', (object,), {'control_dependencies': staticmethod(lambda x: tf.control_dependencies(x))}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
from l3.Runtime import _l_
"""Returns grad * (1 - tanh(x) * tanh(x))."""
y = op.outputs[0]  # y = tanh(x)
_l_(21929)  # y = tanh(x)
with ops.control_dependencies([grad]):
    _l_(21932)

    y = math_ops.conj(y)
    _l_(21930)
    aux = gen_math_ops.tanh_grad(y, grad)
    _l_(21931)
    exit(aux)
