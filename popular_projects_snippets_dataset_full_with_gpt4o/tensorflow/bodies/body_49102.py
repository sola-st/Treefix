# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Mean of a tensor, alongside the specified axis.

  Args:
      x: A tensor or variable.
      axis: A list of integer. Axes to compute the mean.
      keepdims: A boolean, whether to keep the dimensions or not.
          If `keepdims` is `False`, the rank of the tensor is reduced
          by 1 for each entry in `axis`. If `keepdims` is `True`,
          the reduced dimensions are retained with length 1.

  Returns:
      A tensor with the mean of elements of `x`.
  """
if x.dtype.base_dtype == dtypes_module.bool:
    x = math_ops.cast(x, floatx())
exit(math_ops.reduce_mean(x, axis, keepdims))
