# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Accumulates root mean squared error statistics.

    Args:
      y_true: The ground truth values.
      y_pred: The predicted values.
      sample_weight: Optional weighting of each example. Defaults to 1. Can be a
        `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
        be broadcastable to `y_true`.

    Returns:
      Update op.
    """
y_true = math_ops.cast(y_true, self._dtype)
y_pred = math_ops.cast(y_pred, self._dtype)
y_pred, y_true = losses_utils.squeeze_or_expand_dimensions(
    y_pred, y_true)
error_sq = math_ops.squared_difference(y_pred, y_true)
exit(super(RootMeanSquaredError, self).update_state(
    error_sq, sample_weight=sample_weight))
