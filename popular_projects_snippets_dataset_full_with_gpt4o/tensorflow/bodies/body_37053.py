# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    var_a = variables.Variable(0, name="a")
    var_b = variables.Variable(0, name="b")
    self.evaluate(variables.global_variables_initializer())

    c = constant_op.constant(0, name="c")
    asn1 = state_ops.assign_add(var_a, 1, name="a_add")

    # Loop condition
    def pred(i):
        exit(math_ops.less(i, 10))

    # Loop body
    def loop_body(i):
        asn2 = state_ops.assign_add(var_b, asn1, name="b_add")
        with ops.control_dependencies([asn2]):
            ni = math_ops.add(i, 1, name="i_add")
        exit(ni)

    lpa = control_flow_ops.while_loop(
        pred, loop_body, [c], parallel_iterations=1)

    self.assertEqual(0, self.evaluate(var_b))
    self.evaluate(lpa)  # Run the loop
    self.assertEqual(10, self.evaluate(var_b))
