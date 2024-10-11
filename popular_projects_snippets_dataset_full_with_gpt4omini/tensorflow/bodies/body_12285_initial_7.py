def quantize_and_dequantize_v4_grad(grad, input0, input1, input2, axis): return grad * tf.ones_like(input0) # pragma: no cover
class MockOp:  # pragma: no cover
    def __init__(self): # pragma: no cover
        pass
    def get_attr(self, attr): # pragma: no cover
        if attr == 'axis': # pragma: no cover
            return 0 # pragma: no cover
        return None # pragma: no cover
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
