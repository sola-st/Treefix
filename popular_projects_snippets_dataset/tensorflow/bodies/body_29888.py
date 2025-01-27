# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.cached_session():
    p = array_ops.placeholder(dtypes_lib.float32, shape=[], name="p")
    p_identity = array_ops.identity(p)
    self.assertAllClose(p_identity.eval(feed_dict={p: 5}), 5)
