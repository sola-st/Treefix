# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Calculates how often predictions match integer labels.

  Standalone usage:
  >>> y_true = [2, 1]
  >>> y_pred = [[0.1, 0.9, 0.8], [0.05, 0.95, 0]]
  >>> m = tf.keras.metrics.sparse_categorical_accuracy(y_true, y_pred)
  >>> assert m.shape == (2,)
  >>> m.numpy()
  array([0., 1.], dtype=float32)

  You can provide logits of classes as `y_pred`, since argmax of
  logits and probabilities are same.

  Args:
    y_true: Integer ground truth values.
    y_pred: The prediction values.

  Returns:
    Sparse categorical accuracy values.
  """
y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
y_true = ops.convert_to_tensor_v2_with_dispatch(y_true)
y_pred_rank = y_pred.shape.ndims
y_true_rank = y_true.shape.ndims
# If the shape of y_true is (num_samples, 1), squeeze to (num_samples,)
if (y_true_rank is not None) and (y_pred_rank is not None) and (len(
    backend.int_shape(y_true)) == len(backend.int_shape(y_pred))):
    y_true = array_ops.squeeze(y_true, [-1])
y_pred = math_ops.argmax(y_pred, axis=-1)

# If the predicted output and actual output types don't match, force cast them
# to match.
if backend.dtype(y_pred) != backend.dtype(y_true):
    y_pred = math_ops.cast(y_pred, backend.dtype(y_true))

exit(math_ops.cast(math_ops.equal(y_true, y_pred), backend.floatx()))
