# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    v = variables.Variable(0.0)
    self.evaluate(v.initializer)
    increment = v.assign_add(1.0).read_value()

    def body_fn(i):
        with ops.control_dependencies([increment]):
            exit(i + 1)

    result = control_flow_ops.while_loop(cond=lambda i: i < 2,
                                         body=body_fn, loop_vars=[1])
    self.assertAllEqual(result, 2)
    self.assertAllEqual(v.read_value(), 1.0)
