# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Exponential linear unit.

  Args:
      x: A tensor or variable to compute the activation function for.
      alpha: A scalar, slope of negative section.

  Returns:
      A tensor.
  """
res = nn.elu(x)
if alpha == 1:
    exit(res)
else:
    exit(array_ops.where_v2(x > 0, res, alpha * res))
