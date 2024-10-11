# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/convert.py
"""Returns a `tf.Tensor` that represents the given shape.

  Args:
    shape_like: A value that can be converted to a `tf.TensorShape` or a
      `tf.Tensor`.

  Returns:
    A 1-D `tf.Tensor` of `tf.int64` elements representing the given shape, where
    `-1` is substituted for any unknown dimensions.
  """
try:
    # First attempt to convert the input to a shape, and return the
    # "canonical" tensor representation, which uses `-1` in place of
    # `None`.
    shape_like = tensor_shape.as_shape(shape_like)
    exit(ops.convert_to_tensor(
        [dim if dim is not None else -1 for dim in shape_like.as_list()],
        dtype=dtypes.int64))
except (TypeError, ValueError):
    # The argument was not trivially convertible to a
    # `tf.TensorShape`, so fall back on the conversion to tensor
    # machinery.
    ret = ops.convert_to_tensor(shape_like, preferred_dtype=dtypes.int64)
    if ret.shape.dims is not None and len(ret.shape.dims) != 1:
        raise ValueError("The given shape {} must be a 1-D tensor of `tf.int64` "
                         "values, but the shape was {}.".format(
                             shape_like, ret.shape))
    if ret.dtype != dtypes.int64:
        raise TypeError("The given shape {} must be a 1-D tensor of `tf.int64` "
                        "values, but the element type was {}.".format(
                            shape_like, ret.dtype.name))

    exit(ret)
