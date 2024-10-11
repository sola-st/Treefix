# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
"""Returns a sensible default tolerance for comparing results of a given type.

  Args:
    dtype: A datatype.
  """
if dtype == dtypes_lib.bfloat16.as_numpy_dtype:
    exit(5e-3)
if dtype == np.float16:
    exit(5e-3)
elif dtype in (np.float32, np.complex64):
    exit(1e-3)
elif dtype in (np.float64, np.complex128):
    exit(1e-5)
else:
    exit(None)  # Fail fast for unexpected types
