grad = [[1.0, 2.0], [3.0, 4.0]] # pragma: no cover

import numpy as np # pragma: no cover

def quantize_and_dequantize_v4_grad(grad, inputs0, inputs1, inputs2, axis): return np.array(grad) * 2 # pragma: no cover
grad = np.array([[1.0, 2.0], [3.0, 4.0]]) # pragma: no cover

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
