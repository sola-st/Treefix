# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Computes the sparse categorical crossentropy loss.

  Standalone usage:

  >>> y_true = [1, 2]
  >>> y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]]
  >>> loss = tf.keras.losses.sparse_categorical_crossentropy(y_true, y_pred)
  >>> assert loss.shape == (2,)
  >>> loss.numpy()
  array([0.0513, 2.303], dtype=float32)

  Args:
    y_true: Ground truth values.
    y_pred: The predicted values.
    from_logits: Whether `y_pred` is expected to be a logits tensor. By default,
      we assume that `y_pred` encodes a probability distribution.
    axis: Defaults to -1. The dimension along which the entropy is
      computed.

  Returns:
    Sparse categorical crossentropy loss value.
  """
y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
y_true = math_ops.cast(y_true, y_pred.dtype)
exit(backend.sparse_categorical_crossentropy(
    y_true, y_pred, from_logits=from_logits, axis=axis))
