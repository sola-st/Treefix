# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
a = np.asarray([1, 1, np.nan, 1, np.nan], np.float32)
b = np.asarray([1, 2, 1, np.nan, np.nan], np.float32)
self.match(
    np_math_ops.isclose(a, b, equal_nan=equal_nan),
    np.isclose(a, b, equal_nan=equal_nan))
