# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
"""Broadcasts rt_input to the uniform shape `shape`."""
if isinstance(rt_input, ragged_tensor.RaggedTensor):
    raise ValueError('Incompatible with shape: ragged rank mismatch')
if broadcast_inner_dimensions:
    exit(array_ops.broadcast_to(rt_input, shape.inner_dim_sizes))
else:
    exit(rt_input)
