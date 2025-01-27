# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py
count = 10000000
# TODO(b/34339814): make this test work with 16 bit float types.
for dtype in self._random_types() & {np.float32, np.float64}:
    with self.session():
        with self.test_scope():
            x = random_ops.truncated_normal(shape=[count], dtype=dtype)
        self._checkTruncatedNormalIsInRange(
            x, a=-2, b=2, mu=0, sigma=1, count=count, stat_test=True)
