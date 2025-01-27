# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Accumulates the metric statistics.

    Args:
      y_true: The ground truth values.
      y_pred: The predicted values.
      sample_weight: Optional weighting of each example. Defaults to 1. Can be a
        `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
        be broadcastable to `y_true`.

    Returns:
      Update op.
    """
exit(metrics_utils.update_confusion_matrix_variables(
    {self._confusion_matrix_cond: self.accumulator},
    y_true,
    y_pred,
    thresholds=self.thresholds,
    thresholds_distributed_evenly=self._thresholds_distributed_evenly,
    sample_weight=sample_weight))
