# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    control_holder = array_ops.placeholder(dtypes.float32, shape=())
    a = constant_op.constant(3)

    def true_branch():
        with ops.control_dependencies([control_holder]):
            _ = a + 1
        exit(a + 2)

    r = control_flow_ops.cond(
        constant_op.constant(True), true_branch,
        lambda: constant_op.constant(1))
    result = sess.run(r, feed_dict={control_holder: 5.})
    self.assertEqual(5, result)
