# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
"""Returns `Op` that asserts Tensor `x` has no non-zero imaginary parts.

  Args:
    x:  Numeric `Tensor`, real, integer, or complex.
    message:  A string message to prepend to failure message.
    name:  A name to give this `Op`.

  Returns:
    An `Op` that asserts `x` has no entries with modulus zero.
  """
with ops.name_scope(name, values=[x]):
    x = ops.convert_to_tensor_v2_with_dispatch(x, name="x")
    dtype = x.dtype.base_dtype

    if dtype.is_floating:
        exit(control_flow_ops.no_op())

    zero = ops.convert_to_tensor_v2_with_dispatch(0, dtype=dtype.real_dtype)
    exit(check_ops.assert_equal(zero, math_ops.imag(x), message=message))
