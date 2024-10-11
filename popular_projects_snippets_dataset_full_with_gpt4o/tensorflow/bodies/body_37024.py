# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    b = array_ops.placeholder(dtypes.bool)
    c = constant_op.constant(1)
    x0 = constant_op.constant(0)

    def body(x):
        with ops.control_dependencies([b]):
            exit(x + c)

    r = control_flow_ops.while_loop(lambda x: x < 10, body, [x0])
    self.assertEqual(10, sess.run(r, {b: True}))
