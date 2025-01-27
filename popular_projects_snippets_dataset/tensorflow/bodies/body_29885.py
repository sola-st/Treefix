# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.cached_session():
    p = array_ops.placeholder(dtypes_lib.float32, shape=(10, 10), name="p")
    p_identity = array_ops.identity(p)
    feed_array = np.random.rand(10, 10)
    self.assertAllClose(
        p_identity.eval(feed_dict={p: feed_array}), feed_array)

    with self.assertRaisesOpError(
        "must feed a value for placeholder tensor 'p' with dtype float"):
        self.evaluate(p_identity)
