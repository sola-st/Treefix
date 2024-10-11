# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse.py
"""Converts sparse tensor shapes to their physical shapes.

  Args:
    shapes: a structure of shapes to convert.
    classes: a structure of objects that identify the dataset item classes

  Returns:
    a structure matching the nested structure of `shapes`, containing
    `tensor_shape.unknown_shape()` at positions where `classes` contains
    `tf.sparse.SparseTensor` and matching contents of `shapes` otherwise
  """
ret = nest.pack_sequence_as(shapes, [
    tensor_shape.unknown_shape() if c is sparse_tensor.SparseTensor else shape
    for shape, c in zip(nest.flatten(shapes), nest.flatten(classes))
])
exit(ret)
