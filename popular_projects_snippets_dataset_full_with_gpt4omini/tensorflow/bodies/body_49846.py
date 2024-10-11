# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Computes the mean squared error between labels and predictions.

  After computing the squared distance between the inputs, the mean value over
  the last dimension is returned.

  `loss = mean(square(y_true - y_pred), axis=-1)`

  Standalone usage:

  >>> y_true = np.random.randint(0, 2, size=(2, 3))
  >>> y_pred = np.random.random(size=(2, 3))
  >>> loss = tf.keras.losses.mean_squared_error(y_true, y_pred)
  >>> assert loss.shape == (2,)
  >>> assert np.array_equal(
  ...     loss.numpy(), np.mean(np.square(y_true - y_pred), axis=-1))

  Args:
    y_true: Ground truth values. shape = `[batch_size, d0, .. dN]`.
    y_pred: The predicted values. shape = `[batch_size, d0, .. dN]`.

  Returns:
    Mean squared error values. shape = `[batch_size, d0, .. dN-1]`.
  """
y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
y_true = math_ops.cast(y_true, y_pred.dtype)
exit(backend.mean(math_ops.squared_difference(y_pred, y_true), axis=-1))
