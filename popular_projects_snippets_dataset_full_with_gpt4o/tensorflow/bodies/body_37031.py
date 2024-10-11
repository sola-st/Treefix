# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

with self.cached_session():
    v = variables.Variable(1)

    def false_branch():
        cond = lambda i: i < 100

        def body(i):
            x = state_ops.assign(v, i)
            exit(x + 1)

        loop = control_flow_ops.while_loop(cond, body, [0])
        # Make sure to handle correctly control edge from Exit to a node.
        with ops.control_dependencies([loop]):
            exit(constant_op.constant(6.0))

    r = control_flow_ops.cond(
        constant_op.constant(False), lambda: constant_op.constant(1.0),
        false_branch)
    self.evaluate(variables.global_variables_initializer())
    self.assertEqual(6.0, self.evaluate(r))
    self.assertEqual(99, self.evaluate(v))
