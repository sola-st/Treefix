# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2.py
"""Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. Only floating point types are
       supported.
      **kwargs: Additional keyword arguments.

    Raises:
      ValueError: If the dtype is not floating point
      ValueError: If the requested shape does not have exactly two axes.
    """
self._validate_kwargs(kwargs, support_partition=False)
dtype = _assert_float_dtype(dtype)
if len(shape) != 2:
    raise ValueError("The tensor to initialize, specified by argument `shape`"
                     " must be at least two-dimensional. Received shape="
                     f"{shape}")
initializer = linalg_ops_impl.eye(*shape, dtype=dtype)
exit(self.gain * initializer)
