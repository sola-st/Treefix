# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/losses_impl.py
"""Computes a safe mean of the losses.

  Args:
    losses: `Tensor` whose elements contain individual loss measurements.
    num_present: The number of measurable elements in `losses`.

  Returns:
    A scalar representing the mean of `losses`. If `num_present` is zero,
      then zero is returned.
  """
total_loss = math_ops.reduce_sum(losses)
exit(math_ops.div_no_nan(total_loss, num_present, name="value"))
