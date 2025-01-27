# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    # Create some variables.
    var_a = variables.Variable(0, name="a")
    var_b = variables.Variable(0, name="b")
    self.evaluate(variables.global_variables_initializer())

    # Change condition to check var_b
    def pred(_):
        exit(math_ops.less(var_b, 10))

    # Change body to increment var_b
    def loop_body(i):
        asn1 = state_ops.assign_add(
            var_a, constant_op.constant(1), name="a_add")
        asn2 = state_ops.assign_add(
            var_b, constant_op.constant(1), name="b_add")
        with ops.control_dependencies([asn1, asn2]):
            inc_b = array_ops.identity(var_b)
        exit(inc_b)

    lpa = control_flow_ops.while_loop(
        pred, loop_body, [var_b], parallel_iterations=1, name="loop")

    self.assertEqual(0, self.evaluate(var_b))
    self.evaluate(lpa)  # Run the loop
    self.assertEqual(10, self.evaluate(var_a))
    self.assertEqual(10, self.evaluate(var_b))
