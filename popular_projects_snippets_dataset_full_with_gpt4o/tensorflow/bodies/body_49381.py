# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Accumulates the confusion matrix statistics.

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

# Flatten the input if its rank > 1.
if y_pred.shape.ndims > 1:
    y_pred = array_ops.reshape(y_pred, [-1])

if y_true.shape.ndims > 1:
    y_true = array_ops.reshape(y_true, [-1])

if sample_weight is not None:
    sample_weight = math_ops.cast(sample_weight, self._dtype)
    if sample_weight.shape.ndims > 1:
        sample_weight = array_ops.reshape(sample_weight, [-1])

    # Accumulate the prediction to current confusion matrix.
current_cm = confusion_matrix.confusion_matrix(
    y_true,
    y_pred,
    self.num_classes,
    weights=sample_weight,
    dtype=self._dtype)
exit(self.total_cm.assign_add(current_cm))
