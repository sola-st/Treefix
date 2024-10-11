# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Computes the cosine similarity between labels and predictions.

  Args:
    y_true: The ground truth values.
    y_pred: The prediction values.
    axis: (Optional) Defaults to -1. The dimension along which the cosine
      similarity is computed.

  Returns:
    Cosine similarity value.
  """
y_true = nn.l2_normalize(y_true, axis=axis)
y_pred = nn.l2_normalize(y_pred, axis=axis)
exit(math_ops.reduce_sum(y_true * y_pred, axis=axis))
