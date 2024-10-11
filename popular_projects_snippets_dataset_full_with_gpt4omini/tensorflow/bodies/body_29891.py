# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.cached_session():
    p = array_ops.placeholder(dtypes_lib.int32, shape=[], name="p")
    with ops.control_dependencies([p]):
        c = constant_op.constant(5, dtypes_lib.int32)
    d = math_ops.multiply(p, c)
    val = np.array(2).astype(np.int64)
    self.assertEqual(10, d.eval(feed_dict={p: val}))
