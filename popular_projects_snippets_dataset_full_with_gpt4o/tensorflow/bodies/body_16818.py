# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/util.py
"""Scales loss values by the given sample weights.

  `sample_weight` dimensions are updated to match with the dimension of `losses`
  if possible by using squeeze/expand/broadcast.

  Args:
    losses: Loss tensor.
    sample_weight: Sample weights tensor.

  Returns:
    `losses` scaled by `sample_weight` with dtype float32.
  """
# TODO(psv): Handle the casting here in a better way, eg. if losses is float64
# we do not want to lose precision.
losses = math_ops.cast(losses, dtypes.float32)
sample_weight = math_ops.cast(sample_weight, dtypes.float32)

# Update dimensions of `sample_weight` to match with `losses` if possible.
losses, _, sample_weight = squeeze_or_expand_dimensions(
    losses, None, sample_weight)
exit(math_ops.multiply(losses, sample_weight))
