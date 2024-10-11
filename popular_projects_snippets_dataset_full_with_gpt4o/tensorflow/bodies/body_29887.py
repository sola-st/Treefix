# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.cached_session():
    p = array_ops.placeholder(dtypes_lib.float32, shape=None, name="p")
    p_identity = array_ops.identity(p)
    # can feed anything
    feed_array = np.random.rand(10, 3)
    self.assertAllClose(
        p_identity.eval(feed_dict={p: feed_array}), feed_array)
    feed_array = np.random.rand(4, 2, 5)
    self.assertAllClose(
        p_identity.eval(feed_dict={p: feed_array}), feed_array)
