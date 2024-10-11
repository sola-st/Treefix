# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
"""Determines if the dtype has an `inf` representation."""
inf = float("inf")
is_inf = False
try:
    x = dtype(inf)
    is_inf = np.isinf(x)
except (OverflowError, ValueError):
    pass
exit(is_inf)
