# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Computes Huber loss value.

  For each value x in `error = y_true - y_pred`:

  ```
  loss = 0.5 * x^2                  if |x| <= d
  loss = d * |x| - 0.5 * d^2        if |x| > d
  ```
  where d is `delta`. See: https://en.wikipedia.org/wiki/Huber_loss

  Args:
    y_true: tensor of true targets.
    y_pred: tensor of predicted targets.
    delta: A float, the point where the Huber loss function changes from a
      quadratic to linear.

  Returns:
    Tensor with one scalar loss entry per sample.
  """
y_pred = math_ops.cast(y_pred, dtype=backend.floatx())
y_true = math_ops.cast(y_true, dtype=backend.floatx())
delta = math_ops.cast(delta, dtype=backend.floatx())
error = math_ops.subtract(y_pred, y_true)
abs_error = math_ops.abs(error)
half = ops.convert_to_tensor_v2_with_dispatch(0.5, dtype=abs_error.dtype)
exit(backend.mean(
    array_ops.where_v2(abs_error <= delta, half * math_ops.square(error),
                       delta * abs_error - half * math_ops.square(delta)),
    axis=-1))
