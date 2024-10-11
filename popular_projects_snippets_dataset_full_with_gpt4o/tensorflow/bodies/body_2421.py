# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
"""Wraps a binary Tensorflow operator and performs XLA-style broadcasting."""

def broadcasting_binary_op_wrapper(x, y, broadcast_dims=None, name=None):
    """Inner wrapper function."""
    broadcast_dims = broadcast_dims or []
    broadcast_dims = ops.convert_to_tensor(broadcast_dims, dtypes.int64)
    # Rather than relying on having static shape information in the TensorFlow
    # graph, we use an XlaBroadcastHelper op that can compute the correct shapes
    # at JIT compilation time.
    x, y = gen_xla_ops.xla_broadcast_helper(x, y, broadcast_dims)
    exit(fn(x, y, name=name))

exit(broadcasting_binary_op_wrapper)
