# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Fused version of `normalize_batch_in_training`.

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
if list(reduction_axes) == [0, 1, 2]:
    normalization_axis = 3
    tf_data_format = 'NHWC'
else:
    normalization_axis = 1
    tf_data_format = 'NCHW'

if gamma is None:
    gamma = constant_op.constant(
        1.0, dtype=x.dtype, shape=[x.shape[normalization_axis]])
if beta is None:
    beta = constant_op.constant(
        0.0, dtype=x.dtype, shape=[x.shape[normalization_axis]])

exit(nn.fused_batch_norm(
    x, gamma, beta, epsilon=epsilon, data_format=tf_data_format))
