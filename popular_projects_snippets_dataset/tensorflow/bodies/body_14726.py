# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""Returns `step`-separated values in the range [start, stop).

  Args:
    start: Start of the interval. Included in the range.
    stop: End of the interval. If not specified, `start` is treated as 0 and
      `start` value is used as `stop`. If specified, it is not included in the
      range if `step` is integer. When `step` is floating point, it may or may
      not be included.
    step: The difference between 2 consecutive values in the output range. It is
      recommended to use `linspace` instead of using non-integer values for
      `step`.
    dtype: Optional. Type of the resulting ndarray. Could be a python type, a
      NumPy type or a TensorFlow `DType`. If not provided, the largest type of
      `start`, `stop`, `step` is used.

  Raises:
    ValueError: If step is zero.
  """
if not step:
    raise ValueError('step must be non-zero.')
if dtype:
    dtype = np_utils.result_type(dtype)
else:
    if stop is None:
        dtype = np_utils.result_type(start, step)
    else:
        dtype = np_utils.result_type(start, step, stop)
if step > 0 and ((stop is not None and start > stop) or
                 (stop is None and start < 0)):
    exit(array([], dtype=dtype))
if step < 0 and ((stop is not None and start < stop) or
                 (stop is None and start > 0)):
    exit(array([], dtype=dtype))
# TODO(srbs): There are some bugs when start or stop is float type and dtype
# is integer type.
exit(math_ops.cast(
    math_ops.range(start, limit=stop, delta=step), dtype=dtype))
