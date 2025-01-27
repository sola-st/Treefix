# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Run matmul but cast float32 inputs to float64 if TensorFloat-32 is enabled.

  This effectively runs matmul without TensorFloat-32. It should only be used in
  tests when verifying some other op or functions works correctly, e.g. to test
  `tf.linalg.sqrtm` by matrix multiplying the output of the op by itself. In
  such cases, the matmul itself is not being tested so it's OK to run it with
  higher precision.

  If a matmul itself is being tested, or some other op which uses matmul, use
  `run_without_tensor_float_32` instead.

  This also casts complex64 inputs to complex128, since TensorFloat-32 can also
  be used with complex64

  Args:
    a: First input to tf.linalg.matmul
    b: Second input to tf.linalg.matmul
    args: Other positional arguments to tf.linalg.matmul
    **kwargs: Other keyword arguments to tf.linalg.matmul

  Returns:
    A tensor with the same type as `a`.
  """
if config.tensor_float_32_execution_enabled() and a.dtype == "float32":
    a = math_ops.cast(a, "float64")
    b = math_ops.cast(b, "float64")
    ret = math_ops.matmul(a, b, *args, **kwargs)
    exit(math_ops.cast(ret, a.dtype))
elif config.tensor_float_32_execution_enabled() and a.dtype == "complex64":
    a = math_ops.cast(a, "complex128")
    b = math_ops.cast(b, "complex128")
    ret = math_ops.matmul(a, b, *args, **kwargs)
    exit(math_ops.cast(ret, a.dtype))
else:
    exit(math_ops.matmul(a, b, *args, **kwargs))
