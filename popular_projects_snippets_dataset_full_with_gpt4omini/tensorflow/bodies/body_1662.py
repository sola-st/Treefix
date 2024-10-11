# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
with self.session() as sess, self.test_scope():
    for dtype in self._random_types(include_int=True):
        maxval = 1
        if dtype.is_integer:
            maxval = 100
        seed_t = array_ops.placeholder(dtypes.int32, shape=[2])
        x = stateless.stateless_random_uniform(
            shape=[1000], seed=seed_t, maxval=maxval, dtype=dtype)
        y = sess.run(x, {seed_t: [0x12345678, 0xabcdef1]})
        self.assertTrue(np.all(y >= 0))
        self.assertTrue(np.all(y < maxval))
