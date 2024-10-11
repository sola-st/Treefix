# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Compute the exponential moving average of a value.

  The moving average 'x' is updated with 'value' following:

  ```
  x = x * momentum + value * (1 - momentum)
  ```

  For example:

  >>> x = tf.Variable(0.0)
  >>> momentum=0.9
  >>> moving_average_update(x, value = 2.0, momentum=momentum).numpy()
  >>> x.numpy()
  0.2

  The result will be biased towards the initial value of the variable.

  If the variable was initialized to zero, you can divide by
  `1 - momentum ** num_updates` to debias it (Section 3 of
  [Kingma et al., 2015](https://arxiv.org/abs/1412.6980)):

  >>> num_updates = 1.0
  >>> x_zdb = x/(1 - momentum**num_updates)
  >>> x_zdb.numpy()
  2.0

  Args:
      x: A Variable, the moving average.
      value: A tensor with the same shape as `x`, the new value to be
        averaged in.
      momentum: The moving average momentum.

  Returns:
      The updated variable.
  """
if tf2.enabled():
    momentum = math_ops.cast(momentum, x.dtype)
    value = math_ops.cast(value, x.dtype)
    exit(x.assign(x * momentum + value * (1 - momentum)))
else:
    exit(moving_averages.assign_moving_average(
        x, value, momentum, zero_debias=True))
