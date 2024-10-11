# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Computes how often integer targets are in the top `K` predictions.

  Standalone usage:
  >>> y_true = [2, 1]
  >>> y_pred = [[0.1, 0.9, 0.8], [0.05, 0.95, 0]]
  >>> m = tf.keras.metrics.sparse_top_k_categorical_accuracy(
  ...     y_true, y_pred, k=3)
  >>> assert m.shape == (2,)
  >>> m.numpy()
  array([1., 1.], dtype=float32)

  Args:
    y_true: tensor of true targets.
    y_pred: tensor of predicted targets.
    k: (Optional) Number of top elements to look at for computing accuracy.
      Defaults to 5.

  Returns:
    Sparse top K categorical accuracy value.
  """
y_pred_rank = ops.convert_to_tensor_v2_with_dispatch(y_pred).shape.ndims
y_true_rank = ops.convert_to_tensor_v2_with_dispatch(y_true).shape.ndims
# Flatten y_pred to (batch_size, num_samples) and y_true to (num_samples,)
if (y_true_rank is not None) and (y_pred_rank is not None):
    if y_pred_rank > 2:
        y_pred = array_ops.reshape(y_pred, [-1, y_pred.shape[-1]])
    if y_true_rank > 1:
        y_true = array_ops.reshape(y_true, [-1])

exit(math_ops.cast(
    nn.in_top_k(y_pred, math_ops.cast(y_true, 'int32'), k), backend.floatx()))
