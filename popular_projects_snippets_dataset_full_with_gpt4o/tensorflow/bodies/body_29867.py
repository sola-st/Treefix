# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.cached_session():
    h = array_ops.placeholder(dtypes_lib.int32, shape=[])
    w = array_ops.placeholder(dtypes_lib.int32, shape=[])
    z = array_ops.ones([h, w])
    out = z.eval(feed_dict={h: 4, w: 16})
self.assertAllEqual(out, np.array([[1] * 16] * 4))
