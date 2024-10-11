# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py
# TODO(b/112289993): Make this test work with dtype np.float64.
for dtype in self._random_types() & {np.float32}:
    with self.session():
        with self.test_scope():
            count = 10000000
            a = -100.
            b = 100.
            mu0 = 0.
            mu1 = 1.
            sigma = .1
            x = random_ops.parameterized_truncated_normal(
                shape=[2, count],
                dtype=dtype,
                means=[mu0, mu1],
                stddevs=sigma,
                minvals=[a],
                maxvals=[b])
        self._checkTruncatedNormalIsInRange(
            x[0], a=a, b=b, mu=mu0, sigma=sigma, count=count, stat_test=True)
        self._checkTruncatedNormalIsInRange(
            x[1], a=a, b=b, mu=mu1, sigma=sigma, count=count, stat_test=True)
