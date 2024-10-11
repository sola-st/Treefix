# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
tensor_list = gen_sparse_ops.deserialize_sparse(tensor_list[0], self._dtype)
indices, values, dense_shape = tensor_list
rank = self._shape.ndims
indices.set_shape([None, rank])
# We restore the dense_shape from the SparseTypeSpec. This is necessary
# for shape inference when using placeholder SparseTensors in function
# tracing.
if self._shape.is_fully_defined():
    dense_shape = ops.convert_to_tensor(
        self._shape, dtype=dtypes.int64, name="shape")
elif (self._shape.rank is not None and
      any(dim.value is not None for dim in self._shape.dims)):
    # array_ops imports sparse_tensor.py. Local import to avoid import cycle.
    from tensorflow.python.ops import array_ops  # pylint: disable=g-import-not-at-top
    pieces = array_ops.unstack(dense_shape, num=self._shape.rank)
    for i, dim in enumerate(self._shape.dims):
        if dim.value is not None:
            pieces[i] = constant_op.constant(dim.value, dense_shape.dtype)
    dense_shape = array_ops.stack(pieces)
else:
    dense_shape.set_shape([rank])

exit(SparseTensor(indices, values, dense_shape))
