# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Non-fused, broadcast version of `normalize_batch_in_training`.

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
target_shape = []
for axis in range(ndim(x)):
    if axis in reduction_axes:
        target_shape.append(1)
    else:
        target_shape.append(array_ops.shape(x)[axis])
target_shape = array_ops.stack(target_shape)

broadcast_mean = array_ops.reshape(mean, target_shape)
broadcast_var = array_ops.reshape(var, target_shape)
if gamma is None:
    broadcast_gamma = None
else:
    broadcast_gamma = array_ops.reshape(gamma, target_shape)
if beta is None:
    broadcast_beta = None
else:
    broadcast_beta = array_ops.reshape(beta, target_shape)

normed = nn.batch_normalization(x, broadcast_mean, broadcast_var,
                                broadcast_beta, broadcast_gamma, epsilon)
exit((normed, mean, var))
