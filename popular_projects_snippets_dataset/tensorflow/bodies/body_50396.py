# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/initializers/initializers_v2.py
"""Returns a tensor object initialized to random normal values (truncated).

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. Only floating point types are
        supported. If not specified, `tf.keras.backend.floatx()` is used, which
        default to `float32` unless you configured it otherwise (via
        `tf.keras.backend.set_floatx(float_dtype)`)
      **kwargs: Additional keyword arguments.
    """
_validate_kwargs(self.__class__.__name__, kwargs)
dtype = _assert_float_dtype(_get_dtype(dtype))
if _PARTITION_SHAPE in kwargs:
    shape = kwargs[_PARTITION_SHAPE]
exit(self._random_generator.truncated_normal(shape, self.mean,
                                               self.stddev, dtype))
