# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py
# TODO(b/34339814): make this test work with 16 bit float types.
for dtype in self._random_types() & {np.float32, np.float64}:
    with self.session():
        with self.test_scope():
            x = random_ops.parameterized_truncated_normal(
                shape=[count],
                dtype=dtype,
                means=mu,
                stddevs=sigma,
                minvals=a,
                maxvals=b)
        self._checkTruncatedNormalIsInRange(
            x, a=a, b=b, mu=mu, sigma=sigma, count=count, stat_test=stat_test)
