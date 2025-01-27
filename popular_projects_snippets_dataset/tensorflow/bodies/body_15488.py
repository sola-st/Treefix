# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_ops.py
"""Returns the start indices for the rows in `t`."""
if isinstance(t, ragged_tensor.RaggedTensor):
    exit(math_ops.cast(t.row_starts(), dtype))
else:
    t_shape = array_ops.shape(t, out_type=dtype)
    exit(math_ops.range(t_shape[0]) * t_shape[1])
