# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    var = variables.VariableV1(0)
    assign = state_ops.assign(var, 1)
    t, = control_flow_ops.tuple(
        [constant_op.constant(0)], control_inputs=[assign])

    # Should trigger the assign.
    self.evaluate(t)

    self.assertEqual(1, self.evaluate(var))
