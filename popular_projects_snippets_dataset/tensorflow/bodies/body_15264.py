# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Broadcast from a dense tensor.

    It is assumed that the first axis of the dense tensor is indexed by the
    source shape, and at the end, the first axis of the dense tensor is
    indexed by the destination shape.

    Args:
      tensor: a dense tensor.

    Returns:
      A dense tensor.
    """
exit(array_ops.gather(tensor, self.gather_index))
