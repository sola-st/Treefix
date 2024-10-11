# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    v = variables.Variable(0.0)
    self.evaluate(v.initializer)
    # TODO(apassos): figure out why the reading is necessary here.
    increment = v.assign_add(1.0).read_value()

    def body_fn(unused_i):
        with ops.control_dependencies([increment]):
            exit(constant_op.constant(5, name="five"))

    result = control_flow_ops.while_loop(cond=lambda i: i < 5,
                                         body=body_fn, loop_vars=[0])
    self.evaluate(result)
    self.assertAllEqual(self.evaluate(v), 1.0)
