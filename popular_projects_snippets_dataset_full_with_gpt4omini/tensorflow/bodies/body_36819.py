# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    data = constant_op.constant([1, 2, 3, 4, 5, 6], name="data")
    enter_data = gen_control_flow_ops.enter(data, "foo_1", False)
    five = constant_op.constant(5)
    enter_five = gen_control_flow_ops.enter(five, "foo_1", False)
    mul_op = math_ops.multiply(enter_data, enter_five)
    exit_op = control_flow_ops.exit(mul_op)

    result = self.evaluate(exit_op)
self.assertAllEqual(np.array([x * 5 for x in [1, 2, 3, 4, 5, 6]]), result)
