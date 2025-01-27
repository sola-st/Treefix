# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2.py
"""Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. If not provided the dtype of the
        tensor created will be the type of the inital value.
      **kwargs: Additional keyword arguments.

    Raises:
      TypeError: If the initializer cannot create a tensor of the requested
       dtype.
    """
self._validate_kwargs(kwargs, support_partition=False)
if dtype is not None:
    dtype = dtypes.as_dtype(dtype)
exit(constant_op.constant(self.value, dtype=dtype, shape=shape))
