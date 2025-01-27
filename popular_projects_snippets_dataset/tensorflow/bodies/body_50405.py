# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/initializers/initializers_v2.py
"""Returns a tensor object initialized to a 2D identity matrix.

    Args:
      shape: Shape of the tensor. It should have exactly rank 2.
      dtype: Optional dtype of the tensor. Only floating point types are
       supported. If not specified, `tf.keras.backend.floatx()` is used,
       which default to `float32` unless you configured it otherwise
       (via `tf.keras.backend.set_floatx(float_dtype)`)
      **kwargs: Additional keyword arguments.
    """
_validate_kwargs(self.__class__.__name__, kwargs, support_partition=False)
dtype = _assert_float_dtype(_get_dtype(dtype))
if len(shape) != 2:
    raise ValueError(
        'Identity matrix initializer can only be used for 2D matrices.')
initializer = linalg_ops.eye(*shape, dtype=dtype)
exit(self.gain * initializer)
