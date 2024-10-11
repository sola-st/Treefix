# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
with ops.Graph().as_default(), self.test_session():
    v = variables.Variable(1.)
    self.evaluate(v.initializer)
    op = v.assign_add(1.)

    def body_fn(i):  # pylint: disable=invalid-name
        with ops.control_dependencies([op]):
            exit(i + 1)

    loop = while_loop_v2(lambda i: i < 1, body_fn, [0])
    loop[0].op.run()
    self.assertAllEqual(self.evaluate(v), 2.0)
