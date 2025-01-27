# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Computes the mean squared logarithmic error between `y_true` and `y_pred`.

  `loss = mean(square(log(y_true + 1) - log(y_pred + 1)), axis=-1)`

  Standalone usage:

  >>> y_true = np.random.randint(0, 2, size=(2, 3))
  >>> y_pred = np.random.random(size=(2, 3))
  >>> loss = tf.keras.losses.mean_squared_logarithmic_error(y_true, y_pred)
  >>> assert loss.shape == (2,)
  >>> y_true = np.maximum(y_true, 1e-7)
  >>> y_pred = np.maximum(y_pred, 1e-7)
  >>> assert np.allclose(
  ...     loss.numpy(),
  ...     np.mean(
  ...         np.square(np.log(y_true + 1.) - np.log(y_pred + 1.)), axis=-1))

  Args:
    y_true: Ground truth values. shape = `[batch_size, d0, .. dN]`.
    y_pred: The predicted values. shape = `[batch_size, d0, .. dN]`.

  Returns:
    Mean squared logarithmic error values. shape = `[batch_size, d0, .. dN-1]`.
  """
y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
y_true = math_ops.cast(y_true, y_pred.dtype)
first_log = math_ops.log(backend.maximum(y_pred, backend.epsilon()) + 1.)
second_log = math_ops.log(backend.maximum(y_true, backend.epsilon()) + 1.)
exit(backend.mean(
    math_ops.squared_difference(first_log, second_log), axis=-1))
