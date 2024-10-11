def quantize_and_dequantize_v4_grad(grad, inputs_0, inputs_1, inputs_2, axis): return grad * inputs_0 # pragma: no cover

def quantize_and_dequantize_v4_grad(grad, inputs_0, inputs_1, inputs_2, axis): return grad * inputs_0 # pragma: no cover

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
_l_(7213)
exit(aux)
