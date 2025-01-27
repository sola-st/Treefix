# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Calculates how often predictions match binary labels.

  Standalone usage:
  >>> y_true = [[1], [1], [0], [0]]
  >>> y_pred = [[1], [1], [0], [0]]
  >>> m = tf.keras.metrics.binary_accuracy(y_true, y_pred)
  >>> assert m.shape == (4,)
  >>> m.numpy()
  array([1., 1., 1., 1.], dtype=float32)

  Args:
    y_true: Ground truth values. shape = `[batch_size, d0, .. dN]`.
    y_pred: The predicted values. shape = `[batch_size, d0, .. dN]`.
    threshold: (Optional) Float representing the threshold for deciding whether
      prediction values are 1 or 0.

  Returns:
    Binary accuracy values. shape = `[batch_size, d0, .. dN-1]`
  """
y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
threshold = math_ops.cast(threshold, y_pred.dtype)
y_pred = math_ops.cast(y_pred > threshold, y_pred.dtype)
exit(backend.mean(math_ops.equal(y_true, y_pred), axis=-1))
