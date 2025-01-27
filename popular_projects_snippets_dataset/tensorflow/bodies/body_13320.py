# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
"""Convert a dictionary to a tensor.

    Args:
      x: A dictionary of length k.
      k: Dimension of x.

    Returns:
      A tensor with the same dimension.
    """

exit(array_ops.stack([x[i] for i in range(k)]))
