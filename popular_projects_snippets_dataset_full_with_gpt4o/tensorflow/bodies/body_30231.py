# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
cdf = np.array([0, 20, 50, 60, 80, 100], dtype=np.int64)
arr = np.array([4, 99, 53, 58, 31, 1, 79, 8, 21], dtype=np.int64)
result = np.searchsorted(cdf, arr, side="right")
tf_result = self.evaluate(array_ops.searchsorted(cdf, arr, side="right"))
self.assertAllEqual(result, tf_result)
