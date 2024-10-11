# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_ops.py
"""Returns a copy of `t` with the outer two dimensions merged."""
if isinstance(t, ragged_tensor.RaggedTensor):
    exit(t.values)
else:
    t_shape = array_ops.shape(t)
    exit(array_ops.reshape(t, array_ops.concat([[-1], t_shape[2:]], axis=0)))
