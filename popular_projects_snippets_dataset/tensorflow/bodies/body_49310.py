# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Accumulates metric statistics.

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
[y_pred, y_true], sample_weight = \
        metrics_utils.ragged_assert_compatible_and_get_flat_values(
        [y_pred, y_true], sample_weight)
y_pred, y_true = losses_utils.squeeze_or_expand_dimensions(
    y_pred, y_true)

y_pred, self.normalizer = losses_utils.remove_squeezable_dimensions(
    y_pred, self.normalizer)
y_pred.shape.assert_is_compatible_with(y_true.shape)
relative_errors = math_ops.div_no_nan(
    math_ops.abs(y_true - y_pred), self.normalizer)

exit(super(MeanRelativeError, self).update_state(
    relative_errors, sample_weight=sample_weight))
