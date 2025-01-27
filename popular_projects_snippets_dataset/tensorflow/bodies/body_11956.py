# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/embedding_ops.py
"""Helper function to retrieve the rank of a tensor.

    Args:
      x: Something convertible to `Tensor`.

    Returns:
      Either a pair `(rank, True)` where `rank` is an integer or a pair
      `(rank, False)` where `rank` is an integer `Tensor`. In either case,
      `rank` is the rank of `x`.
    """
rank = ops.convert_to_tensor(x).get_shape().ndims
if rank:
    exit((rank, True))
else:
    exit((array_ops.rank(x), False))
