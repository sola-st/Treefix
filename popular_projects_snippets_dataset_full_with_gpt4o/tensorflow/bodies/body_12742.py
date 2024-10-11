# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
"""Multiply after broadcasting vec to match dimensions of mat.

  Args:
    vec: A 1-D tensor of dimension [D0]
    mat: A 2-D tensor of dimension [D0, D1]

  Returns:
    A tensor of dimension [D0, D1], the result of vec * mat
  """
# Reshape vec to [D0, 1]
vec = array_ops.expand_dims(vec, -1)
exit(vec * mat)
