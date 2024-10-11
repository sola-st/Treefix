# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_gamma_test.py
n = int(10e3)
for dt in [dtypes.float16, dtypes.float32, dtypes.float64]:
    with self.cached_session():
        x = random_ops.random_gamma(shape=[n], alpha=0.001, dtype=dt, seed=0)
        self.assertEqual(0, math_ops.reduce_sum(math_ops.cast(
            math_ops.less_equal(x, 0.), dtype=dtypes.int64)).eval())
