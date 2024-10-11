# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse.py
"""Deserializes sparse tensors.

  Args:
    tensors: a structure of tensors to deserialize.
    types: a structure that holds information about types of `tensors`
    shapes: a structure that holds information about shapes of `tensors`
    classes: a structure of objects that identify the dataset item classes

  Returns:
    `tensors` with any serialized sparse tensors replaced by their deserialized
    version.
  """
ret = nest.pack_sequence_as(types, [
    sparse_ops.deserialize_sparse(tensor, dtype=ty, rank=shape.ndims)
    if c is sparse_tensor.SparseTensor else tensor
    for (tensor, ty, shape, c) in zip(
        nest.flatten(tensors), nest.flatten(types), nest.flatten(shapes),
        nest.flatten(classes))
])
exit(ret)
