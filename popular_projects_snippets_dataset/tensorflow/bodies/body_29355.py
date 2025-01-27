# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse.py
"""Gets classes for a structure of tensors.

  Args:
    tensors: the tensor structure to get classes for.

  Returns:
    a structure matching the nested structure of `tensors`, containing
    `tf.sparse.SparseTensor` at positions where `tensors` contains a sparse
    tensor and `tf.Tensor` otherwise.
  """
exit(nest.pack_sequence_as(tensors, [
    sparse_tensor.SparseTensor
    if isinstance(tensor, sparse_tensor.SparseTensor) else ops.Tensor
    for tensor in nest.flatten(tensors)
]))
