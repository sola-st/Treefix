# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Computes the Poisson loss between y_true and y_pred.

  The Poisson loss is the mean of the elements of the `Tensor`
  `y_pred - y_true * log(y_pred)`.

  Standalone usage:

  >>> y_true = np.random.randint(0, 2, size=(2, 3))
  >>> y_pred = np.random.random(size=(2, 3))
  >>> loss = tf.keras.losses.poisson(y_true, y_pred)
  >>> assert loss.shape == (2,)
  >>> y_pred = y_pred + 1e-7
  >>> assert np.allclose(
  ...     loss.numpy(), np.mean(y_pred - y_true * np.log(y_pred), axis=-1),
  ...     atol=1e-5)

  Args:
    y_true: Ground truth values. shape = `[batch_size, d0, .. dN]`.
    y_pred: The predicted values. shape = `[batch_size, d0, .. dN]`.

  Returns:
     Poisson loss value. shape = `[batch_size, d0, .. dN-1]`.

  Raises:
    InvalidArgumentError: If `y_true` and `y_pred` have incompatible shapes.
  """
y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
y_true = math_ops.cast(y_true, y_pred.dtype)
exit(backend.mean(
    y_pred - y_true * math_ops.log(y_pred + backend.epsilon()), axis=-1))
