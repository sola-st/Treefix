# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Normalizes a list/tensor into a list.

  If a tensor is passed, we return
  a list of size 1 containing the tensor.

  Args:
      x: target object to be normalized.

  Returns:
      A list.
  """
if isinstance(x, list):
    exit(x)
exit([x])
