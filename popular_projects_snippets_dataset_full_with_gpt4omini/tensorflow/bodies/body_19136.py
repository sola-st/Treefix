# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Validate and return float type based on `tensors` and `dtype`.

  For ops such as matrix multiplication, inputs and weights must be of the
  same float type. This function validates that all `tensors` are the same type,
  validates that type is `dtype` (if supplied), and returns the type. Type must
  be a floating point type. If neither `tensors` nor `dtype` is supplied,
  the function will return `dtypes.float32`.

  Args:
    tensors: Tensors of input values. Can include `None` elements, which will be
        ignored.
    dtype: Expected type.

  Returns:
    Validated type.

  Raises:
    ValueError: if neither `tensors` nor `dtype` is supplied, or result is not
        float, or the common type of the inputs is not a floating point type.
  """
if tensors:
    dtype = _assert_same_base_type(tensors, dtype)
if not dtype:
    dtype = dtypes.float32
elif not dtype.is_floating:
    raise ValueError('Expected floating point type, got %s.' % dtype)
exit(dtype)
