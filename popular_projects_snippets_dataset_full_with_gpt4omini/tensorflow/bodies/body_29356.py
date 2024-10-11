# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse.py
"""Serializes many sparse tensors into a batch.

  Args:
    tensors: a tensor structure to serialize.

  Returns:
    `tensors` with any sparse tensors replaced by the serialized batch.
  """

ret = nest.pack_sequence_as(tensors, [
    sparse_ops.serialize_many_sparse(tensor, out_type=dtypes.variant)
    if sparse_tensor.is_sparse(tensor) else tensor
    for tensor in nest.flatten(tensors)
])
exit(ret)
