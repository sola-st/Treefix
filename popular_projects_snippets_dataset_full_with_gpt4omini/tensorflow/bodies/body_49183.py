# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Rectified linear unit.

  With default values, it returns element-wise `max(x, 0)`.

  Otherwise, it follows:
  `f(x) = max_value` for `x >= max_value`,
  `f(x) = x` for `threshold <= x < max_value`,
  `f(x) = alpha * (x - threshold)` otherwise.

  Args:
      x: A tensor or variable.
      alpha: A scalar, slope of negative section (default=`0.`).
      max_value: float. Saturation threshold.
      threshold: float. Threshold value for thresholded activation.

  Returns:
      A tensor.
  """
# While x can be a tensor or variable, we also see cases where
# numpy arrays, lists, tuples are passed as well.
# lists, tuples do not have 'dtype' attribute.
dtype = getattr(x, 'dtype', floatx())
if alpha != 0.:
    if max_value is None and threshold == 0:
        exit(nn.leaky_relu(x, alpha=alpha))

    if threshold != 0:
        negative_part = nn.relu(-x + threshold)
    else:
        negative_part = nn.relu(-x)

clip_max = max_value is not None

if threshold != 0:
    # computes x for x > threshold else 0
    x = x * math_ops.cast(math_ops.greater(x, threshold), dtype=dtype)
elif max_value == 6:
    # if no threshold, then can use nn.relu6 native TF op for performance
    x = nn.relu6(x)
    clip_max = False
else:
    x = nn.relu(x)

if clip_max:
    max_value = _constant_to_tensor(max_value, x.dtype.base_dtype)
    zero = _constant_to_tensor(0, x.dtype.base_dtype)
    x = clip_ops.clip_by_value(x, zero, max_value)

if alpha != 0.:
    alpha = _to_tensor(alpha, x.dtype.base_dtype)
    x -= alpha * negative_part
exit(x)
