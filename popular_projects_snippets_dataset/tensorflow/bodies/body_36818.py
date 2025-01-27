# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    v = variables.VariableV1(7)

    p = constant_op.constant(True)
    v1 = control_flow_ops._SwitchRefOrTensor(v._ref(), p)  # pylint: disable=protected-access
    v2 = state_ops.assign(v1[1], 9)
    self.evaluate(variables.global_variables_initializer())
    self.assertEqual(9, self.evaluate(v2))
