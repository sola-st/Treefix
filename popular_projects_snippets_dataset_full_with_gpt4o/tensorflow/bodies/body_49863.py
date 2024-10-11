# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Computes the categorical hinge loss between `y_true` and `y_pred`.

  `loss = maximum(neg - pos + 1, 0)`
  where `neg=maximum((1-y_true)*y_pred) and pos=sum(y_true*y_pred)`

  Standalone usage:

  >>> y_true = np.random.randint(0, 3, size=(2,))
  >>> y_true = tf.keras.utils.to_categorical(y_true, num_classes=3)
  >>> y_pred = np.random.random(size=(2, 3))
  >>> loss = tf.keras.losses.categorical_hinge(y_true, y_pred)
  >>> assert loss.shape == (2,)
  >>> pos = np.sum(y_true * y_pred, axis=-1)
  >>> neg = np.amax((1. - y_true) * y_pred, axis=-1)
  >>> assert np.array_equal(loss.numpy(), np.maximum(0., neg - pos + 1.))

  Args:
    y_true: The ground truth values. `y_true` values are expected to be
    either `{-1, +1}` or `{0, 1}` (i.e. a one-hot-encoded tensor).
    y_pred: The predicted values.

  Returns:
    Categorical hinge loss values.
  """
y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
y_true = math_ops.cast(y_true, y_pred.dtype)
pos = math_ops.reduce_sum(y_true * y_pred, axis=-1)
neg = math_ops.reduce_max((1. - y_true) * y_pred, axis=-1)
zero = math_ops.cast(0., y_pred.dtype)
exit(math_ops.maximum(neg - pos + 1., zero))
