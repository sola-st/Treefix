# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/indexed_slices.py
"""Constructs a type specification for a `tf.IndexedSlices`.

    Args:
      shape: The dense shape of the `IndexedSlices`, or `None` to allow any
        dense shape.
      dtype: `tf.DType` of values in the `IndexedSlices`.
      indices_dtype: `tf.DType` of the `indices` in the `IndexedSlices`.  One
        of `tf.int32` or `tf.int64`.
      dense_shape_dtype: `tf.DType` of the `dense_shape` in the `IndexedSlices`.
        One of `tf.int32`, `tf.int64`, or `None` (if the `IndexedSlices` has
        no `dense_shape` tensor).
      indices_shape: The shape of the `indices` component, which indicates
        how many slices are in the `IndexedSlices`.
    """
self._shape = tensor_shape.as_shape(shape)
self._values_dtype = dtypes.as_dtype(dtype)
self._indices_dtype = dtypes.as_dtype(indices_dtype)
if dense_shape_dtype is None:
    self._dense_shape_dtype = None
else:
    self._dense_shape_dtype = dtypes.as_dtype(dense_shape_dtype)
self._indices_shape = tensor_shape.as_shape(indices_shape).with_rank(1)
