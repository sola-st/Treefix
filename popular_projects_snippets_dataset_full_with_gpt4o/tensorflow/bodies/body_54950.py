# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
"""Constructs a type specification for a `tf.sparse.SparseTensor`.

    Args:
      shape: The dense shape of the `SparseTensor`, or `None` to allow any dense
        shape.
      dtype: `tf.DType` of values in the `SparseTensor`.
    """
self._shape = tensor_shape.as_shape(shape)
self._dtype = dtypes.as_dtype(dtype)
