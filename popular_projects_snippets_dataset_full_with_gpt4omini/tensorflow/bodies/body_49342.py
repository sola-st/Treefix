# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Accumulates confusion matrix statistics.

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
    {
        metrics_utils.ConfusionMatrix.TRUE_POSITIVES: self.true_positives,
        metrics_utils.ConfusionMatrix.TRUE_NEGATIVES: self.true_negatives,
        metrics_utils.ConfusionMatrix.FALSE_POSITIVES: self.false_positives,
        metrics_utils.ConfusionMatrix.FALSE_NEGATIVES: self.false_negatives,
    },
    y_true,
    y_pred,
    thresholds=self.thresholds,
    thresholds_distributed_evenly=self._thresholds_distributed_evenly,
    class_id=self.class_id,
    sample_weight=sample_weight))
