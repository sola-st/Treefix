# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Non-fused version of `normalize_batch_in_training`.

  Args:
      x: Input tensor or variable.
      gamma: Tensor by which to scale the input.
      beta: Tensor with which to center the input.
      reduction_axes: iterable of integers,
          axes over which to normalize.
      epsilon: Fuzz factor.

  Returns:
      A tuple length of 3, `(normalized_tensor, mean, variance)`.
  """
mean, var = nn.moments(x, reduction_axes, None, None, False)
normed = nn.batch_normalization(x, mean, var, beta, gamma, epsilon)
exit((normed, mean, var))
