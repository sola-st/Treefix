# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Pads `value` to the front and/or back of a `Tensor` dim, `count` times.

  Args:
    x: `Tensor` input.
    axis: Scalar `int`-like `Tensor` representing the single dimension to pad.
      (Negative indexing is supported.)
    front: Python `bool`; if `True` the beginning of the `axis` dimension is
      padded with `value`, `count` times. If `False` no front padding is made.
    back: Python `bool`; if `True` the end of the `axis` dimension is padded
      with `value`, `count` times. If `False` no end padding is made.
    value: Scalar `int`-like `Tensor` representing the actual value added to the
      front and/or back of the `axis` dimension of `x`.
    count: Scalar `int`-like `Tensor` representing number of elements added to
      the front and/or back of the `axis` dimension of `x`. E.g., if `front =
      back = True` then `2 * count` elements are added.
    name: Python `str` name prefixed to Ops created by this function.

  Returns:
    pad: The padded version of input `x`.

  Raises:
    ValueError: if both `front` and `back` are `False`.
    TypeError: if `count` is not `int`-like.
  """
with ops.name_scope(name, "pad", [x, value, count]):
    x = ops.convert_to_tensor(x, name="x")
    value = ops.convert_to_tensor(value, dtype=x.dtype, name="value")
    count = ops.convert_to_tensor(count, name="count")
    if not count.dtype.is_integer:
        raise TypeError("`count.dtype` (`{}`) must be `int`-like.".format(
            count.dtype.name))
    if not front and not back:
        raise ValueError("At least one of `front`, `back` must be `True`.")
    ndims = (
        x.shape.ndims if x.shape.ndims is not None else array_ops.rank(
            x, name="ndims"))
    axis = ops.convert_to_tensor(axis, name="axis")
    axis_ = tensor_util.constant_value(axis)
    if axis_ is not None:
        axis = axis_
        if axis < 0:
            axis = ndims + axis
        count_ = tensor_util.constant_value(count)
        if axis_ >= 0 or x.shape.ndims is not None:
            head = x.shape[:axis]
            middle = tensor_shape.TensorShape(None if count_ is None else (
                tensor_shape.dimension_at_index(x.shape, axis) + count_ *
                (front + back)))
            tail = x.shape[axis + 1:]
            final_shape = head.concatenate(middle.concatenate(tail))
        else:
            final_shape = None
    else:
        axis = array_ops.where_v2(axis < 0, ndims + axis, axis)
        final_shape = None
    x = array_ops.pad(
        x,
        paddings=array_ops.one_hot(
            indices=array_ops.stack(
                [axis if front else -1, axis if back else -1]),
            depth=ndims,
            axis=0,
            on_value=count,
            dtype=dtypes.int32),
        constant_values=value)
    if final_shape is not None:
        x.set_shape(final_shape)
    exit(x)
