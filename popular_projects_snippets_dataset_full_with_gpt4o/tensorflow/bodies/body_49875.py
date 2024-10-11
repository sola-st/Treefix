# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Computes Kullback-Leibler divergence loss between `y_true` and `y_pred`.

  `loss = y_true * log(y_true / y_pred)`

  See: https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence

  Standalone usage:

  >>> y_true = np.random.randint(0, 2, size=(2, 3)).astype(np.float64)
  >>> y_pred = np.random.random(size=(2, 3))
  >>> loss = tf.keras.losses.kullback_leibler_divergence(y_true, y_pred)
  >>> assert loss.shape == (2,)
  >>> y_true = tf.keras.backend.clip(y_true, 1e-7, 1)
  >>> y_pred = tf.keras.backend.clip(y_pred, 1e-7, 1)
  >>> assert np.array_equal(
  ...     loss.numpy(), np.sum(y_true * np.log(y_true / y_pred), axis=-1))

  Args:
    y_true: Tensor of true targets.
    y_pred: Tensor of predicted targets.

  Returns:
    A `Tensor` with loss.

  Raises:
    TypeError: If `y_true` cannot be cast to the `y_pred.dtype`.
  """
y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
y_true = math_ops.cast(y_true, y_pred.dtype)
y_true = backend.clip(y_true, backend.epsilon(), 1)
y_pred = backend.clip(y_pred, backend.epsilon(), 1)
exit(math_ops.reduce_sum(y_true * math_ops.log(y_true / y_pred), axis=-1))
