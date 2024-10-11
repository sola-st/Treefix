# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    select = variables.Variable([3.0, 4.0, 5.0])
    n = constant_op.constant(0)

    def loop_iterator(j):
        exit(math_ops.less(j, 3))

    def loop_body(j):
        ns = state_ops.scatter_update(select, j, 10.0)
        nj = math_ops.add(j, 1)
        op = control_flow_ops.group(ns)
        nj = control_flow_ops.with_dependencies([op], nj)
        exit([nj])

    r = control_flow_ops.while_loop(
        loop_iterator, loop_body, [n], parallel_iterations=1)
    self.evaluate(variables.global_variables_initializer())
    self.assertEqual(3, self.evaluate(r))
    result = self.evaluate(select)
    self.assertAllClose(np.array([10.0, 10.0, 10.0]), result)
