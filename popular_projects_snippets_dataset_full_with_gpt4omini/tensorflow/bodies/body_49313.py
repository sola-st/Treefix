# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Accumulates metric statistics.

    `y_true` and `y_pred` should have the same shape.

    Args:
      y_true: Ground truth values. shape = `[batch_size, d0, .. dN]`.
      y_pred: The predicted values. shape = `[batch_size, d0, .. dN]`.
      sample_weight: Optional `sample_weight` acts as a
        coefficient for the metric. If a scalar is provided, then the metric is
        simply scaled by the given value. If `sample_weight` is a tensor of size
        `[batch_size]`, then the metric for each sample of the batch is rescaled
        by the corresponding element in the `sample_weight` vector. If the shape
        of `sample_weight` is `[batch_size, d0, .. dN-1]` (or can be broadcasted
        to this shape), then each metric element of `y_pred` is scaled by the
        corresponding value of `sample_weight`. (Note on `dN-1`: all metric
        functions reduce by 1 dimension, usually the last axis (-1)).

    Returns:
      Update op.
    """
y_true = math_ops.cast(y_true, self._dtype)
y_pred = math_ops.cast(y_pred, self._dtype)
[y_true, y_pred], sample_weight = (
    metrics_utils.ragged_assert_compatible_and_get_flat_values(
        [y_true, y_pred], sample_weight))
y_pred, y_true = losses_utils.squeeze_or_expand_dimensions(
    y_pred, y_true)

ag_fn = autograph.tf_convert(self._fn, ag_ctx.control_status_ctx())
matches = ag_fn(y_true, y_pred, **self._fn_kwargs)
exit(super(MeanMetricWrapper, self).update_state(
    matches, sample_weight=sample_weight))
