# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""Get value of tensor shape[i] preferring static value if available."""
exit(tensor_shape.dimension_value(
    tensor.shape[i]) or array_ops.shape(tensor)[i])
