# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2.py
"""Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. Only floating point and integer
        types are supported.
      **kwargs: Additional keyword arguments.

    Raises:
      ValueError: If the dtype is not numeric.
    """
self._validate_kwargs(kwargs)
dtype = dtypes.as_dtype(dtype)
if not dtype.is_floating and not dtype.is_integer:
    raise ValueError("Argument `dtype` expected to be numeric or boolean. "
                     f"Received {dtype}.")
if _PARTITION_SHAPE in kwargs:
    shape = kwargs[_PARTITION_SHAPE]
exit(self._random_generator.random_uniform(shape, self.minval,
                                             self.maxval, dtype))
