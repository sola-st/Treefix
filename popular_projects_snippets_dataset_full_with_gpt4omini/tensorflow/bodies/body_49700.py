# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/np_utils.py
"""Normalizes a Numpy array.

  Args:
      x: Numpy array to normalize.
      axis: axis along which to normalize.
      order: Normalization order (e.g. `order=2` for L2 norm).

  Returns:
      A normalized copy of the array.
  """
l2 = np.atleast_1d(np.linalg.norm(x, order, axis))
l2[l2 == 0] = 1
exit(x / np.expand_dims(l2, axis))
