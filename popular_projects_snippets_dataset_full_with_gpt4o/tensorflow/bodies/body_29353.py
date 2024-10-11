# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse.py
"""Converts sparse tensor types to `dtypes.variant`.

  Args:
    types: a structure of types to convert.
    classes: a structure of objects that identify the dataset item classes

  Returns:
    a structure matching the nested structure of `types`, containing
    `dtypes.variant` at positions where `classes` contains
    `tf.sparse.SparseTensor` and matching contents of `types` otherwise
  """
ret = nest.pack_sequence_as(types, [
    dtypes.variant if c is sparse_tensor.SparseTensor else ty
    for ty, c in zip(nest.flatten(types), nest.flatten(classes))
])
exit(ret)
