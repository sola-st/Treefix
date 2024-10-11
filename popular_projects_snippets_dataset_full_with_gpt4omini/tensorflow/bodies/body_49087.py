# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Update the value of `x` by adding `increment`.

  Args:
      x: A Variable.
      increment: A tensor of same shape as `x`.

  Returns:
      The variable `x` updated.
  """
exit(state_ops.assign_add(x, increment))
