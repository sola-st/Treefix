# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
# asin()'s gradient overflows at the value close to 1.0.
exit(math_ops.asin(x) + 1.0)
