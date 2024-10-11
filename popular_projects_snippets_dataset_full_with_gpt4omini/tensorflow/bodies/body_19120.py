# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Assert that `x` is of integer dtype.

  If `x` has a non-integer type, `message`, as well as the dtype of `x` are
  printed, and `InvalidArgumentError` is raised.

  This can always be checked statically, so this method returns nothing.

  Args:
    x: A `Tensor`.
    message: A string to prefix to the default message.
    name: A name for this operation (optional). Defaults to "assert_integer".

  Raises:
    TypeError:  If `x.dtype` is not a non-quantized integer type.
  """
assert_integer(x=x, message=message, name=name)
