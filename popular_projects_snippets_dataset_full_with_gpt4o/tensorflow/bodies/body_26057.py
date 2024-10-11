# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/from_sparse_tensor_slices_op.py
"""See `Dataset.from_sparse_tensor_slices()` for details."""
if not isinstance(sparse_tensor, sparse_tensor_lib.SparseTensor):
    raise TypeError(f"Invalid `sparse_tensor`. `sparse_tensor` must be a "
                    f"`tf.sparse.SparseTensor`. Got {type(sparse_tensor)}.")
self._sparse_tensor = sparse_tensor

indices_shape = self._sparse_tensor.indices.get_shape()
shape_shape = self._sparse_tensor.dense_shape.get_shape()
rank = (indices_shape.dims[1] - 1).merge_with(shape_shape.dims[0] - 1)
self._structure = (tensor_spec.TensorSpec([None, rank], dtypes.int64),
                   tensor_spec.TensorSpec([None],
                                          self._sparse_tensor.dtype),
                   tensor_spec.TensorSpec([rank], dtypes.int64))

variant_tensor = gen_dataset_ops.sparse_tensor_slice_dataset(
    self._sparse_tensor.indices, self._sparse_tensor.values,
    self._sparse_tensor.dense_shape)
super().__init__(variant_tensor)
