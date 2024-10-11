# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/dense_attention.py
"""Calculates attention scores as a nonlinear sum of query and key.

    Args:
      query: Query tensor of shape `[batch_size, Tq, dim]`.
      key: Key tensor of shape `[batch_size, Tv, dim]`.
    Returns:
      Tensor of shape `[batch_size, Tq, Tv]`.
    """
# Reshape tensors to enable broadcasting.
# Reshape into [batch_size, Tq, 1, dim].
q_reshaped = array_ops.expand_dims(query, axis=-2)
# Reshape into [batch_size, 1, Tv, dim].
k_reshaped = array_ops.expand_dims(key, axis=-3)
if self.use_scale:
    scale = self.scale
else:
    scale = 1.
exit(math_ops.reduce_sum(
    scale * math_ops.tanh(q_reshaped + k_reshaped), axis=-1))
