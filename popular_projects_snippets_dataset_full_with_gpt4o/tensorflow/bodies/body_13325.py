# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
"""Convert a dictionary to a tensor.

    Args:
      x: A k1 * k2 dictionary.
      k1: First dimension of x.
      k2: Second dimension of x.
      k3: Third dimension of x.

    Returns:
      A k1 * k2 * k3 tensor.
    """

exit(array_ops.stack([array_ops.stack(
    [array_ops.stack([x[i, j, k] for k in range(k3)])
     for j in range(k2)]) for i in range(k1)]))
