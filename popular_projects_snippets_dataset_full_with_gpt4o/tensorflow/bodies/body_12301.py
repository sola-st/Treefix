# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Return the elements, either from `x` or `y`, depending on the `condition`.

  If both `x` and `y` are None, then this operation returns the coordinates of
  true elements of `condition`.  The coordinates are returned in a 2-D tensor
  where the first dimension (rows) represents the number of true elements, and
  the second dimension (columns) represents the coordinates of the true
  elements. Keep in mind, the shape of the output tensor can vary depending on
  how many true values there are in input. Indices are output in row-major
  order.

  If both non-None, `x` and `y` must have the same shape.
  The `condition` tensor must be a scalar if `x` and `y` are scalar.
  If `x` and `y` are tensors of higher rank, then `condition` must be either a
  vector with size matching the first dimension of `x`, or must have the same
  shape as `x`.

  The `condition` tensor acts as a mask that chooses, based on the value at each
  element, whether the corresponding element / row in the output should be taken
  from `x` (if true) or `y` (if false).

  If `condition` is a vector and `x` and `y` are higher rank matrices, then it
  chooses which row (outer dimension) to copy from `x` and `y`. If `condition`
  has the same shape as `x` and `y`, then it chooses which element to copy from
  `x` and `y`.

  Args:
    condition: A `Tensor` of type `bool`
    x: A Tensor which may have the same shape as `condition`. If `condition` is
      rank 1, `x` may have higher rank, but its first dimension must match the
      size of `condition`.
    y: A `tensor` with the same shape and type as `x`.
    name: A name of the operation (optional)

  Returns:
    A `Tensor` with the same type and shape as `x`, `y` if they are non-None.
    Otherwise, a `Tensor` with shape `(num_true, rank(condition))`.

  Raises:
    ValueError: When exactly one of `x` or `y` is non-None.

  @compatibility(TF2)

  This API is compatible with eager execution and `tf.function`. However, this
  is still a legacy API endpoint originally designed for TF1. To migrate to
  fully-native TF2, please replace its usage with `tf.where` instead, which is
  directly backwards compatible with `tf.compat.v1.where`.

  However,`tf.compat.v1.where` is more restrictive than `tf.where`, requiring
  `x` and `y` to have the same shape, and returning a `Tensor` with the same
  type and shape as `x`, `y` (if they are both non-None).

  `tf.where` will accept `x`, `y` that are not the same shape as long as they
  are broadcastable with one another and with `condition`, and will return a
  `Tensor` with shape broadcast from `condition`, `x`, and `y`.

  For example, the following works with `tf.where` but not `tf.compat.v1.where`:

  >>> tf.where([True, False, False, True], [1,2,3,4], [100])
  <tf.Tensor: shape=(4,), dtype=int32, numpy=array([  1, 100, 100,   4],
  dtype=int32)>

  >>> tf.where(True, [1,2,3,4], 100)
  <tf.Tensor: shape=(4,), dtype=int32, numpy=array([1, 2, 3, 4],
  dtype=int32)>

  @end_compatibility
  """
if x is None and y is None:
    with ops.name_scope(name, "Where", [condition]) as name:
        condition = ops.convert_to_tensor(
            condition, preferred_dtype=dtypes.bool, name="condition")
        exit(gen_array_ops.where(condition=condition, name=name))
elif x is not None and y is not None:
    exit(gen_math_ops.select(condition=condition, x=x, y=y, name=name))
else:
    raise ValueError("x and y must both be non-None or both be None.")
