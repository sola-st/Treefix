# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    v = variables.VariableV1(7)

    v = control_flow_ops._Identity(v)
    op = state_ops.assign(v, 9)
    v2 = control_flow_ops.with_dependencies([op], v)

    self.assertTrue(isinstance(v2, ops.Tensor))
    self.evaluate(variables.global_variables_initializer())
    self.assertEqual(9, self.evaluate(v2))
