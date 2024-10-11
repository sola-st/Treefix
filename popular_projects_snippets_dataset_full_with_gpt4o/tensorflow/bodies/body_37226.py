# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    tensor_list = []

    def condition(t):
        exit(t < constant_op.constant(5))

    def body(_):
        tensor_list.append(constant_op.constant(5))
        exit(constant_op.constant(10))

    result = control_flow_ops.while_loop(condition, body,
                                         [constant_op.constant(4)])
    self.assertEqual(10, self.evaluate(result))

    # Ensure that we cannot run a tensor that escapes the loop body
    # accidentally.
    with self.assertRaises(ValueError):
        sess.run(tensor_list[0])
