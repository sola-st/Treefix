# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    s = gen_data_flow_ops.stack_v2(-1, dtypes.int32, stack_name="foo")
    i = constant_op.constant(0)

    def c(i):
        exit(math_ops.less(i, 10))

    def b(i):
        ni = math_ops.add(i, 1)
        ni = control_flow_ops.with_dependencies(
            [gen_data_flow_ops.stack_push_v2(s, i)], ni)
        exit(ni)

    r = control_flow_ops.while_loop(c, b, [i], parallel_iterations=1)

    x = constant_op.constant(0)

    def c1(i, _):
        exit(math_ops.greater(i, 0))

    def b1(i, x):
        ni = math_ops.subtract(i, 1)
        nx = x + gen_data_flow_ops.stack_pop_v2(s, dtypes.int32)
        exit([ni, nx])

    _, rx = control_flow_ops.while_loop(
        c1,
        b1, [r, x],
        [r.get_shape(), tensor_shape.unknown_shape()],
        parallel_iterations=1)
    self.assertEqual(45, self.evaluate(rx))
