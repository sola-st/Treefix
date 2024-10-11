# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
num_samples = 10000
with self.session():
    np.random.seed(42)
    for dtype in [np.int32, np.float32]:
        arr = np.random.randint(0, 1000, num_samples)
        weights = np.ones(num_samples).astype(dtype)
        self.assertAllClose(
            self.evaluate(bincount_ops.bincount(arr, None)),
            np.bincount(arr, weights))
