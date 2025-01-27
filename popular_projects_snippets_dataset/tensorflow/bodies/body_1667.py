# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
for dtype in self._random_types():
    with self.session() as sess, self.test_scope():
        seed_t = array_ops.placeholder(dtypes.int32, shape=[2])
        n = int(10e7)
        x = stateless.stateless_parameterized_truncated_normal(
            shape=[n],
            seed=seed_t,
            means=means,
            stddevs=stddevs,
            minvals=minvals,
            maxvals=maxvals)
        y = sess.run(x, {seed_t: [0x12345678, 0xabcdef1]})
        if variance_rtol is None:
            variance_rtol = 6e-3 if dtype == dtypes.bfloat16 else 1e-3
        random_test_util.test_truncated_normal(
            self.assertEqual,
            self.assertAllClose,
            n,
            y,
            means=means,
            stddevs=stddevs,
            minvals=minvals,
            maxvals=maxvals,
            mean_atol=1e-3,
            median_atol=1e-3,
            variance_rtol=variance_rtol)
