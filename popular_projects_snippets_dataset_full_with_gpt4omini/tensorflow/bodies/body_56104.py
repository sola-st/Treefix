# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
"""Initializes a new `BoundedTensorSpec`.

    Args:
      shape: Value convertible to `tf.TensorShape`. The shape of the tensor.
      dtype: Value convertible to `tf.DType`. The type of the tensor values.
      minimum: Number or sequence specifying the minimum element bounds
        (inclusive). Must be broadcastable to `shape`.
      maximum: Number or sequence specifying the maximum element bounds
        (inclusive). Must be broadcastable to `shape`.
      name: Optional string containing a semantic name for the corresponding
        array. Defaults to `None`.

    Raises:
      ValueError: If `minimum` or `maximum` are not provided or not
        broadcastable to `shape`.
      TypeError: If the shape is not an iterable or if the `dtype` is an invalid
        numpy dtype.
    """
super(BoundedTensorSpec, self).__init__(shape, dtype, name)

if minimum is None:
    raise ValueError("`minimum` can not be None.")
if maximum is None:
    raise ValueError("`maximum` can not be None.")

try:
    minimum_shape = np.shape(minimum)
    common_shapes.broadcast_shape(
        tensor_shape.TensorShape(minimum_shape), self.shape)
except ValueError as exception:
    raise ValueError(f"`minimum` {minimum} is not compatible with shape "
                     f"{self.shape}. Original error: {exception!r}.")

try:
    maximum_shape = np.shape(maximum)
    common_shapes.broadcast_shape(
        tensor_shape.TensorShape(maximum_shape), self.shape)
except ValueError as exception:
    raise ValueError(f"`maximum` {maximum} is not compatible with shape "
                     f"{self.shape}. Original error: {exception!r}.")

self._minimum = np.array(minimum, dtype=self.dtype.as_numpy_dtype)
self._minimum.setflags(write=False)

self._maximum = np.array(maximum, dtype=self.dtype.as_numpy_dtype)
self._maximum.setflags(write=False)
