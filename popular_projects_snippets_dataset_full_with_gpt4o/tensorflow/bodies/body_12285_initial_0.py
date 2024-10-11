import numpy as np # pragma: no cover

def quantize_and_dequantize_v4_grad(grad, input0, input1, input2, axis):# pragma: no cover
    return np.array([1.0, 2.0, 3.0]) # pragma: no cover
grad = np.array([0.1, 0.2, 0.3]) # pragma: no cover
op = type('Mock', (object,), {'inputs': [np.array([0.5, 1.0, 1.5]), np.array([0.1, 0.2, 0.3]), np.array([0.05, 0.1, 0.15])], 'get_attr': lambda self, attr_name: 0})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
from l3.Runtime import _l_
"""Gradient for QuantizeAndDequantizeV4 op."""
aux = quantize_and_dequantize_v4_grad(
    grad,
    op.inputs[0],
    op.inputs[1],
    op.inputs[2],
    axis=op.get_attr("axis"))
_l_(20202)
exit(aux)
