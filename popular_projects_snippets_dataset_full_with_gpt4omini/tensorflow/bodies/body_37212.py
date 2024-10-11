# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    v0 = variables.Variable(-1)
    v1 = variables.Variable(-1)
    v2 = variables.Variable(-1)

    a = lambda: control_flow_ops.with_dependencies([state_ops.assign(v0, 0)], 0)
    b = lambda: control_flow_ops.with_dependencies([state_ops.assign(v1, 1)], 1)
    c = lambda: control_flow_ops.with_dependencies([state_ops.assign(v2, 2)], 2)

    x = constant_op.constant(1)
    y = constant_op.constant(2)

    r0 = control_flow_ops.case(
        ((x < y, a), (x > y, b)), default=c, exclusive=True)
    r1 = control_flow_ops.case(
        ((x > y, a), (x < y, b)), default=c, exclusive=True)
    r2 = control_flow_ops.case(
        ((x > y, a), (x > y, b)), default=c, exclusive=True)

    self.evaluate(variables.global_variables_initializer())
    self.assertAllEqual(self.evaluate([v0, v1, v2]), [-1] * 3)
    self.assertEqual(2, self.evaluate(r2))
    self.assertAllEqual(self.evaluate([v0, v1, v2]), [-1, -1, 2])

    self.evaluate(variables.global_variables_initializer())
    self.assertAllEqual(self.evaluate([v0, v1, v2]), [-1] * 3)
    self.assertEqual(1, self.evaluate(r1))
    self.assertAllEqual(self.evaluate([v0, v1, v2]), [-1, 1, -1])

    self.evaluate(variables.global_variables_initializer())
    self.assertAllEqual(self.evaluate([v0, v1, v2]), [-1] * 3)
    self.assertEqual(0, self.evaluate(r0))
    self.assertAllEqual(self.evaluate([v0, v1, v2]), [0, -1, -1])
