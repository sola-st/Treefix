# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2.py
"""Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. Only numeric or boolean dtypes are
       supported.
      **kwargs: Additional keyword arguments.

    Raises:
      ValuesError: If the dtype is not numeric or boolean.
    """
self._validate_kwargs(kwargs)
dtype = dtypes.as_dtype(dtype)
if not dtype.is_numpy_compatible or dtype == dtypes.string:
    raise ValueError("Argument `dtype` expected to be numeric or boolean. "
                     f"Received {dtype}.")
if _PARTITION_SHAPE in kwargs:
    shape = kwargs[_PARTITION_SHAPE]
exit(array_ops.zeros(shape, dtype))
