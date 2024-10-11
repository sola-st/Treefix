# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
num_samples = 10000
with self.session():
    np.random.seed(42)
    for dtype in [dtypes.int32, dtypes.int64, dtypes.float32, dtypes.float64]:
        arr = np.random.randint(0, 1000, num_samples)
        if dtype == dtypes.int32 or dtype == dtypes.int64:
            weights = np.random.randint(-100, 100, num_samples)
        else:
            weights = np.random.random(num_samples)
        self.assertAllClose(
            self.evaluate(bincount_ops.bincount(arr, weights)),
            np.bincount(arr, weights))
