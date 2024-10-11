# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Creates a tensor by tiling `x` by `n`.

  Args:
      x: A tensor or variable
      n: A list of integer. The length must be the same as the number of
          dimensions in `x`.

  Returns:
      A tiled tensor.
  """
if isinstance(n, int):
    n = [n]
exit(array_ops.tile(x, n))
