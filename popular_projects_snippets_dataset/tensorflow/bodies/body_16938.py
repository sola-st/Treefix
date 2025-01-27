# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_impl.py
"""Calculate the sufficient statistics for the mean and variance of `x`.

  These sufficient statistics are computed using the one pass algorithm on
  an input that's optionally shifted. See:
  https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Computing_shifted_data

  For example:
  >>> t = [[1, 2, 3], [4, 5, 6]]
  >>> sufficient_statistics(t, [1])
  (<tf.Tensor: shape=(), dtype=int32, numpy=3>, <tf.Tensor: shape=(2,),
  dtype=int32, numpy=array([ 6, 15], dtype=int32)>, <tf.Tensor: shape=(2,),
  dtype=int32, numpy=array([14, 77], dtype=int32)>, None)
  >>> sufficient_statistics(t, [-1])
  (<tf.Tensor: shape=(), dtype=int32, numpy=3>, <tf.Tensor: shape=(2,),
  dtype=int32, numpy=array([ 6, 15], dtype=int32)>, <tf.Tensor: shape=(2,),
  dtype=int32, numpy=array([14, 77], dtype=int32)>, None)

  Args:
    x: A `Tensor`.
    axes: Array of ints. Axes along which to compute mean and variance. As in
      Python, the axes can also be negative numbers. A negative axis is
      interpreted as counting from the end of the rank, i.e., axis +
      rank(values)-th dimension.
    shift: A `Tensor` containing the value by which to shift the data for
      numerical stability, or `None` if no shift is to be performed. A shift
      close to the true mean provides the most numerically stable results.
    keep_dims: produce statistics with the same dimensionality as the input.
    name: Name used to scope the operations that compute the sufficient stats.
    keepdims: Alias for keep_dims.

  Returns:
    Four `Tensor` objects of the same type as `x`:

    * the count (number of elements to average over).
    * the (possibly shifted) sum of the elements in the array.
    * the (possibly shifted) sum of squares of the elements in the array.
    * the shift by which the mean must be corrected or None if `shift` is None.
  """
axes = list(set(axes))
keep_dims = deprecated_argument_lookup(
    "keepdims", keepdims, "keep_dims", keep_dims)
if keep_dims is None:
    keep_dims = False
with ops.name_scope(name, "sufficient_statistics", [x, shift]):
    x = ops.convert_to_tensor(x, name="x")
    x_shape = x.get_shape()
    if x_shape.rank is not None and all(
        x_shape.dims[d].value is not None for d in axes):
        counts = 1
        for d in axes:
            counts *= x_shape.dims[d].value
        counts = constant_op.constant(counts, dtype=x.dtype)
    else:  # shape needs to be inferred at runtime.
        # Normalize axes to be positive. Required for gather.
        rank = array_ops.rank(x)
        positive_axes = [axis + rank if axis < 0 else axis for axis in axes]
        x_dims = array_ops.gather(
            math_ops.cast(array_ops.shape(x), x.dtype), positive_axes)
        counts = math_ops.reduce_prod(x_dims, name="count")
    if shift is not None:
        shift = ops.convert_to_tensor(shift, name="shift")
        m_ss = math_ops.subtract(x, shift)
        v_ss = math_ops.squared_difference(x, shift)
    else:  # no shift.
        m_ss = x
        v_ss = math_ops.square(x)
    m_ss = math_ops.reduce_sum(m_ss, axes, keepdims=keep_dims, name="mean_ss")
    v_ss = math_ops.reduce_sum(v_ss, axes, keepdims=keep_dims, name="var_ss")
exit((counts, m_ss, v_ss, shift))
