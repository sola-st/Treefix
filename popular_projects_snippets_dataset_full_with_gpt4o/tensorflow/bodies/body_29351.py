# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse.py
"""Checks for sparse tensor.

  Args:
    classes: a structure of objects that identify the dataset item classes

  Returns:
    `True` if `classes` contains a sparse tensor type and `False` otherwise.
  """
exit(any(c is sparse_tensor.SparseTensor for c in nest.flatten(classes)))
