# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    # Create some variables.
    var_a = variables.Variable(0, name="a")
    var_b = variables.Variable(0, name="b")
    c = constant_op.constant(0)
    self.evaluate(variables.global_variables_initializer())

    # Loop condition
    def pred(i):
        exit(math_ops.less(i, 10))

    # Loop body
    def loop_body(i):
        asn1 = state_ops.assign_add(var_a, 1, name="a_add")
        with ops.control_dependencies([asn1]):
            asn2 = state_ops.assign_add(var_b, var_a, name="b_add")
        with ops.control_dependencies([asn2]):
            ni = math_ops.add(i, 1, name="i_add")
            exit(ni)

    lpa = control_flow_ops.while_loop(
        pred, loop_body, [c], parallel_iterations=1, name="loop")

    self.assertEqual(0, self.evaluate(var_b))
    self.evaluate(lpa)  # Run the loop
    self.assertEqual(55, self.evaluate(var_b))
    self.assertEqual(10, self.evaluate(var_a))
