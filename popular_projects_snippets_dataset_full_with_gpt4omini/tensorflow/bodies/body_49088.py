# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Update the value of `x` by subtracting `decrement`.

  Args:
      x: A Variable.
      decrement: A tensor of same shape as `x`.

  Returns:
      The variable `x` updated.
  """
exit(state_ops.assign_sub(x, decrement))
