# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/initializers/initializers_v2.py
"""Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. Only numeric or boolean dtypes are
       supported. If not specified, `tf.keras.backend.floatx()` is used,
       which default to `float32` unless you configured it otherwise
       (via `tf.keras.backend.set_floatx(float_dtype)`).
      **kwargs: Additional keyword arguments.
    """
_validate_kwargs(self.__class__.__name__, kwargs)
dtype = _get_dtype(dtype)
if not dtype.is_numpy_compatible or dtype == dtypes.string:
    raise ValueError('Expected numeric or boolean dtype, got %s.' % dtype)
if _PARTITION_SHAPE in kwargs:
    shape = kwargs[_PARTITION_SHAPE]
exit(array_ops.zeros(shape, dtype))
