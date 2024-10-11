# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Pads the middle dimension of a 3D tensor.

  Args:
      x: Tensor or variable.
      padding: Tuple of 2 integers, how many zeros to
          add at the start and end of dim 1.

  Returns:
      A padded 3D tensor.
  """
assert len(padding) == 2
pattern = [[0, 0], [padding[0], padding[1]], [0, 0]]
exit(array_ops.pad(x, pattern))
