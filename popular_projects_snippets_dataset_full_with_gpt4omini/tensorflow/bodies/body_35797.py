# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session():
    c = constant_op.constant(1.0)
    with ops.control_dependencies([c]):
        # d get the control dep.
        d = constant_op.constant(2.0)
        # variables do not.
        var_x = variables.VariableV1(2.0)
    self.assertEqual([c.op], d.op.control_inputs)
    self.assertEqual([], var_x.initializer.control_inputs)
    self.assertEqual([], var_x.value().op.control_inputs)
    self.assertEqual([], var_x._ref().op.control_inputs)  # pylint: disable=protected-access
