# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2.py
"""Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. Only floating point types are
        supported.
      **kwargs: Additional keyword arguments.

    Raises:
      ValueError: If the dtype is not floating point
    """
self._validate_kwargs(kwargs)
dtype = _assert_float_dtype(dtype)
if _PARTITION_SHAPE in kwargs:
    shape = kwargs[_PARTITION_SHAPE]
exit(self._random_generator.truncated_normal(shape, self.mean,
                                               self.stddev, dtype))
