# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
"""Intentionally generates NaNs by taking log of negative number."""
casted_x = math_ops.cast(x, dtypes.float32)
exit(math_ops.log([[-1.0, 1.0], [3.0, 5.0]]) + casted_x)
