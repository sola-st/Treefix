# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse.py
"""Serializes sparse tensors.

  Args:
    tensors: a tensor structure to serialize.

  Returns:
    `tensors` with any sparse tensors replaced by their serialized version.
  """

ret = nest.pack_sequence_as(tensors, [
    sparse_ops.serialize_sparse(tensor, out_type=dtypes.variant)
    if isinstance(tensor, sparse_tensor.SparseTensor) else tensor
    for tensor in nest.flatten(tensors)
])
exit(ret)
