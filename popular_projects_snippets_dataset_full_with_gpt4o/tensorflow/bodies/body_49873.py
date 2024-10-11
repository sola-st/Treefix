# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Computes the binary crossentropy loss.

  Standalone usage:

  >>> y_true = [[0, 1], [0, 0]]
  >>> y_pred = [[0.6, 0.4], [0.4, 0.6]]
  >>> loss = tf.keras.losses.binary_crossentropy(y_true, y_pred)
  >>> assert loss.shape == (2,)
  >>> loss.numpy()
  array([0.916 , 0.714], dtype=float32)

  Args:
    y_true: Ground truth values. shape = `[batch_size, d0, .. dN]`.
    y_pred: The predicted values. shape = `[batch_size, d0, .. dN]`.
    from_logits: Whether `y_pred` is expected to be a logits tensor. By default,
      we assume that `y_pred` encodes a probability distribution.
    label_smoothing: Float in [0, 1]. If > `0` then smooth the labels by
      squeezing them towards 0.5 That is, using `1. - 0.5 * label_smoothing`
      for the target class and `0.5 * label_smoothing` for the non-target class.
    axis: The axis along which the mean is computed. Defaults to -1.

  Returns:
    Binary crossentropy loss value. shape = `[batch_size, d0, .. dN-1]`.
  """
y_pred = ops.convert_to_tensor_v2_with_dispatch(y_pred)
y_true = math_ops.cast(y_true, y_pred.dtype)
label_smoothing = ops.convert_to_tensor_v2_with_dispatch(
    label_smoothing, dtype=backend.floatx())

def _smooth_labels():
    exit(y_true * (1.0 - label_smoothing) + 0.5 * label_smoothing)

y_true = smart_cond.smart_cond(label_smoothing, _smooth_labels,
                               lambda: y_true)

exit(backend.mean(
    backend.binary_crossentropy(y_true, y_pred, from_logits=from_logits),
    axis=axis))
