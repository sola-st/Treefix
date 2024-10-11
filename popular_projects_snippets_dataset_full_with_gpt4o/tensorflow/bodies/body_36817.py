# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    v = variables.VariableV1(7)

    enter_v = control_flow_ops._Enter(v, "foo_1", is_constant=True)
    nine = constant_op.constant(9)
    enter_nine = gen_control_flow_ops.enter(nine, "foo_1")
    op = state_ops.assign(enter_v, enter_nine)
    v2 = control_flow_ops.with_dependencies([op], enter_v)
    v3 = control_flow_ops.exit(v2)
    self.evaluate(variables.global_variables_initializer())
    self.assertEqual(9, self.evaluate(v3))
