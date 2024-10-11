# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
z = x // y
# Numpy produces 0 for INT_MIN/-1, but we expect an overflow to INT_MIN
# so that (INT_MIN/-1) + (INT_MIN % -1) = INT_MIN + 0 = INT_MIN.
z[(x == np.iinfo(x.dtype).min) & (y == -1)] = np.iinfo(x.dtype).min
exit(z)
