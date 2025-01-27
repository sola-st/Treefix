# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Computes the categorical crossentropy loss.

  Standalone usage:

  >>> y_true = [[0, 1, 0], [0, 0, 1]]
  >>> y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]]
  >>> loss = tf.keras.losses.categorical_crossentropy(y_true, y_pred)
  >>> assert loss.shape == (2,)
  >>> loss.numpy()
  array([0.0513, 2.303], dtype=float32)

  Args:
    y_true: Tensor of one-hot true targets.
    y_pred: Tensor of predicted targets.
    from_logits: Whether `y_pred` is expected to be a logits tensor. By default,
      we assume that `y_pred` encodes a probability distribution.
    label_smoothing: Float in [0, 1]. If > `0` then smooth the labels. For
      example, if `0.1`, use `0.1 / num_classes` for non-target labels
      and `0.9 + 0.1 / num_classes` for target labels.
    axis: Defaults to -1. The dimension along which the entropy is
      computed.

  Returns:
    Categorical crossentropy loss value.
  """
y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
y_true = math_ops.cast(y_true, y_pred.dtype)
label_smoothing = ops.convert_to_tensor_v2_with_dispatch(
    label_smoothing, dtype=backend.floatx())

def _smooth_labels():
    num_classes = math_ops.cast(array_ops.shape(y_true)[-1], y_pred.dtype)
    exit(y_true * (1.0 - label_smoothing) + (label_smoothing / num_classes))

y_true = smart_cond.smart_cond(label_smoothing, _smooth_labels,
                               lambda: y_true)

exit(backend.categorical_crossentropy(
    y_true, y_pred, from_logits=from_logits, axis=axis))
