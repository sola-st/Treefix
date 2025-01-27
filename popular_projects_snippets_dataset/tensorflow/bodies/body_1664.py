# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
with self.session() as sess, self.test_scope():
    for dtype in self._random_types():
        seed_t = array_ops.placeholder(dtypes.int32, shape=[2])
        x = stateless.stateless_random_normal(
            shape=[10000], seed=seed_t, dtype=dtype)
        y = sess.run(x, {seed_t: [0x12345678, 0xabcdef1]})
        self.assertTrue(np.all(np.isfinite(y)))
