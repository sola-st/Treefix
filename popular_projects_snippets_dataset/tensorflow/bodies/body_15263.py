# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Create an identity broadcaster.

    TODO(martinz): an identity broadcaster can be far more efficient than a
    generic broadcaster. Add an optimized implementation.
    Args:
      nvals: the number of values for the broadcaster.
      dtype: the dtype of the broadcaster, or None to use the dtype of nvals.

    Returns:
      an identity broadcaster from [0....nvals-1] to [0...nvals-1]
    """
exit(_GatherLayerBroadcaster(math_ops.range(nvals, dtype=dtype)))
