# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py
for dtype in self._random_types() & {np.float32, np.float64}:
    with self.session():
        with self.test_scope():
            a = -1.
            b = 1.
            mu = 0.
            sigma = 1.
            count = 10000000
            x = random_ops.parameterized_truncated_normal(
                shape=[1, count],
                dtype=dtype,
                means=mu,
                stddevs=sigma,
                minvals=[a],
                maxvals=[b])
        self._checkTruncatedNormalIsInRange(
            x, a=a, b=b, mu=mu, sigma=sigma, count=count, stat_test=True)
