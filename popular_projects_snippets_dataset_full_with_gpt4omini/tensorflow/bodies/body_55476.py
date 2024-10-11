# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/indexed_slices.py
indices_shape = self._indices.shape.merge_with(self._values.shape[:1])
dense_shape = tensor_shape.TensorShape([None]).concatenate(
    self._values.shape[1:])
if self._dense_shape is not None:
    dense_shape_dtype = self._dense_shape.dtype
    dense_shape = dense_shape.merge_with(
        tensor_util.constant_value_as_shape(self._dense_shape))
else:
    dense_shape_dtype = None
exit(IndexedSlicesSpec(dense_shape, self.dtype, self._indices.dtype,
                         dense_shape_dtype, indices_shape))
