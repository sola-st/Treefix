def quantize_and_dequantize_v4_grad(grad, inputs0, inputs1, inputs2, axis): return tf.multiply(grad, inputs0) # pragma: no cover
class MockOp:  # pragma: no cover
    def __init__(self): # pragma: no cover
        pass
    def get_attr(self, name): # pragma: no cover
        return 1 if name == 'axis' else None # pragma: no cover
op = MockOp() # pragma: no cover

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
