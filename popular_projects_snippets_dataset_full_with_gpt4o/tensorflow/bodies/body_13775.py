# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Computes `log(abs(sum(weight * exp(elements across tensor dimensions))))`.

  If all weights `w` are known to be positive, it is more efficient to directly
  use `reduce_logsumexp`, i.e., `tf.reduce_logsumexp(logx + tf.math.log(w))` is
  more
  efficient than `du.reduce_weighted_logsumexp(logx, w)`.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keep_dims` is true, the rank of the tensor is reduced by 1 for each
  entry in `axis`. If `keep_dims` is true, the reduced dimensions
  are retained with length 1.

  If `axis` has no entries, all dimensions are reduced, and a
  tensor with a single element is returned.

  This function is more numerically stable than log(sum(w * exp(input))). It
  avoids overflows caused by taking the exp of large inputs and underflows
  caused by taking the log of small inputs.

  For example:

  ```python
  x = tf.constant([[0., 0, 0],
                   [0, 0, 0]])

  w = tf.constant([[-1., 1, 1],
                   [1, 1, 1]])

  du.reduce_weighted_logsumexp(x, w)
  # ==> log(-1*1 + 1*1 + 1*1 + 1*1 + 1*1 + 1*1) = log(4)

  du.reduce_weighted_logsumexp(x, w, axis=0)
  # ==> [log(-1+1), log(1+1), log(1+1)]

  du.reduce_weighted_logsumexp(x, w, axis=1)
  # ==> [log(-1+1+1), log(1+1+1)]

  du.reduce_weighted_logsumexp(x, w, axis=1, keep_dims=True)
  # ==> [[log(-1+1+1)], [log(1+1+1)]]

  du.reduce_weighted_logsumexp(x, w, axis=[0, 1])
  # ==> log(-1+5)
  ```

  Args:
    logx: The tensor to reduce. Should have numeric type.
    w: The weight tensor. Should have numeric type identical to `logx`.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keep_dims: If true, retains reduced dimensions with length 1.
    return_sign: If `True`, returns the sign of the result.
    name: A name for the operation (optional).

  Returns:
    lswe: The `log(abs(sum(weight * exp(x))))` reduced tensor.
    sign: (Optional) The sign of `sum(weight * exp(x))`.
  """
with ops.name_scope(name, "reduce_weighted_logsumexp", [logx, w]):
    logx = ops.convert_to_tensor(logx, name="logx")
    if w is None:
        lswe = math_ops.reduce_logsumexp(logx, axis=axis, keepdims=keep_dims)
        if return_sign:
            sgn = array_ops.ones_like(lswe)
            exit((lswe, sgn))
        exit(lswe)
    w = ops.convert_to_tensor(w, dtype=logx.dtype, name="w")
    log_absw_x = logx + math_ops.log(math_ops.abs(w))
    max_log_absw_x = math_ops.reduce_max(log_absw_x, axis=axis, keepdims=True)
    # If the largest element is `-inf` or `inf` then we don't bother subtracting
    # off the max. We do this because otherwise we'd get `inf - inf = NaN`. That
    # this is ok follows from the fact that we're actually free to subtract any
    # value we like, so long as we add it back after taking the `log(sum(...))`.
    max_log_absw_x = array_ops.where_v2(
        math_ops.is_inf(max_log_absw_x), array_ops.zeros_like(max_log_absw_x),
        max_log_absw_x)
    wx_over_max_absw_x = (
        math_ops.sign(w) * math_ops.exp(log_absw_x - max_log_absw_x))
    sum_wx_over_max_absw_x = math_ops.reduce_sum(
        wx_over_max_absw_x, axis=axis, keepdims=keep_dims)
    if not keep_dims:
        max_log_absw_x = array_ops.squeeze(max_log_absw_x, axis)
    sgn = math_ops.sign(sum_wx_over_max_absw_x)
    lswe = max_log_absw_x + math_ops.log(sgn * sum_wx_over_max_absw_x)
    if return_sign:
        exit((lswe, sgn))
    exit(lswe)
