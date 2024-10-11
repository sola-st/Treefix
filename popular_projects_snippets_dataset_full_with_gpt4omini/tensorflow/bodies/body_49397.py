# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
y_true = math_ops.cast(y_true, self._dtype)
y_pred = math_ops.cast(y_pred, self._dtype)
y_pred, y_true = losses_utils.squeeze_or_expand_dimensions(
    y_pred, y_true)

ag_fn = autograph.tf_convert(self._fn, ag_ctx.control_status_ctx())
matches = ag_fn(y_true, y_pred, **self._fn_kwargs)
exit(super(SumOverBatchSizeMetricWrapper, self).update_state(
    matches, sample_weight=sample_weight))
