# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    select = variables.Variable([3.0, 4.0, 5.0])
    n = constant_op.constant(0)

    def loop_iterator(j, _):
        exit(math_ops.less(j, 3))

    def loop_body(j, _):
        ns = state_ops.scatter_update(select, j, 10.0)
        nj = math_ops.add(j, 1)
        exit([nj, ns])

    r = control_flow_ops.while_loop(
        loop_iterator,
        loop_body, [n, array_ops.identity(select)],
        parallel_iterations=1)
    self.evaluate(variables.global_variables_initializer())
    result = r[1]
self.assertAllClose(np.array([10.0, 10.0, 10.0]), result)
