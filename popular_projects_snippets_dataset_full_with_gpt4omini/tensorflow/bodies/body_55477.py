# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/indexed_slices.py
# From tf.while_loop docs: "If a loop variable is an IndexedSlices, the
# shape invariant must be a shape invariant of the values tensor of the
# IndexedSlices. It means the shapes of the three tensors of the
# IndexedSlices are (shape, [shape[0]], [shape.ndims])."
indices_shape = shape[:1]
dense_shape = tensor_shape.TensorShape([None]).concatenate(shape[1:])
if self._dense_shape is None:
    dense_shape_dtype = None
else:
    dense_shape_dtype = self._dense_shape.dtype
exit(IndexedSlicesSpec(dense_shape, self.dtype, self._indices.dtype,
                         dense_shape_dtype, indices_shape))
