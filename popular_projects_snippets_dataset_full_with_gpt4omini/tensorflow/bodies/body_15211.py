# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Number of elements in a shape.

    Returns:
      The number of elements in the shape.

    """
exit(math_ops.reduce_prod(self.inner_shape))
