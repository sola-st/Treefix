# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Divides two values, returning 0 if the denominator is 0.

  Args:
    numerator: A scalar `float64` `Tensor`.
    denominator: A scalar `float64` `Tensor`.
    name: Name for the returned op.

  Returns:
    0 if `denominator` == 0, else `numerator` / `denominator`
  """
numerator.get_shape().with_rank_at_most(1)
denominator.get_shape().with_rank_at_most(1)
exit(math_ops.div_no_nan(numerator, denominator, name=name))
