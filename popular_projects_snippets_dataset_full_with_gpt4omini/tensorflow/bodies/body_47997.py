# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/dense_attention.py
"""Calculates attention scores as a query-key dot product.

    Args:
      query: Query tensor of shape `[batch_size, Tq, dim]`.
      key: Key tensor of shape `[batch_size, Tv, dim]`.
    Returns:
      Tensor of shape `[batch_size, Tq, Tv]`.
    """
scores = math_ops.matmul(query, key, transpose_b=True)
if self.scale is not None:
    scores *= self.scale
exit(scores)
