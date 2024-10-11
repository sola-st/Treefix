# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
with self.session() as sess, self.test_scope():
    seed_t = array_ops.placeholder(dtypes.int32, shape=[2])
    means = array_ops.zeros([2], dtype=dtypes.float32)
    stddevs = array_ops.ones([3, 1], dtype=dtypes.float32)
    minvals = -array_ops.ones([5, 1, 1], dtype=dtypes.float32)
    maxvals = array_ops.ones([7, 1, 1, 1], dtype=dtypes.float32)
    shape = [11, 7, 5, 3, 2]
    x = stateless.stateless_parameterized_truncated_normal(
        shape=shape,
        seed=seed_t,
        means=means,
        stddevs=stddevs,
        minvals=minvals,
        maxvals=maxvals)
    y = sess.run(x, {seed_t: [0x12345678, 0xabcdef1]})
    self.assertEqual((11, 7, 5, 3, 2), y.shape)
