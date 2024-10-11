# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Computes the mean absolute percentage error between `y_true` and `y_pred`.

  `loss = 100 * mean(abs((y_true - y_pred) / y_true), axis=-1)`

  Standalone usage:

  >>> y_true = np.random.random(size=(2, 3))
  >>> y_true = np.maximum(y_true, 1e-7)  # Prevent division by zero
  >>> y_pred = np.random.random(size=(2, 3))
  >>> loss = tf.keras.losses.mean_absolute_percentage_error(y_true, y_pred)
  >>> assert loss.shape == (2,)
  >>> assert np.array_equal(
  ...     loss.numpy(),
  ...     100. * np.mean(np.abs((y_true - y_pred) / y_true), axis=-1))

  Args:
    y_true: Ground truth values. shape = `[batch_size, d0, .. dN]`.
    y_pred: The predicted values. shape = `[batch_size, d0, .. dN]`.

  Returns:
    Mean absolute percentage error values. shape = `[batch_size, d0, .. dN-1]`.
  """
y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
y_true = math_ops.cast(y_true, y_pred.dtype)
diff = math_ops.abs(
    (y_true - y_pred) / backend.maximum(math_ops.abs(y_true),
                                        backend.epsilon()))
exit(100. * backend.mean(diff, axis=-1))
