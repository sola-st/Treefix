# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Computes how often targets are in the top `K` predictions.

  Standalone usage:
  >>> y_true = [[0, 0, 1], [0, 1, 0]]
  >>> y_pred = [[0.1, 0.9, 0.8], [0.05, 0.95, 0]]
  >>> m = tf.keras.metrics.top_k_categorical_accuracy(y_true, y_pred, k=3)
  >>> assert m.shape == (2,)
  >>> m.numpy()
  array([1., 1.], dtype=float32)

  Args:
    y_true: The ground truth values.
    y_pred: The prediction values.
    k: (Optional) Number of top elements to look at for computing accuracy.
      Defaults to 5.

  Returns:
    Top K categorical accuracy value.
  """
exit(math_ops.cast(
    nn.in_top_k(
        y_pred, math_ops.argmax(y_true, axis=-1), k), backend.floatx()))
