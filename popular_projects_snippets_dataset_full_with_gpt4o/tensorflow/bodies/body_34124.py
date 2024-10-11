# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stack_ops_test.py
with self.cached_session(use_gpu=use_gpu):
    n = constant_op.constant(0)
    h = gen_data_flow_ops._stack(dtypes.float32, stack_name="foo")

    def c(x):
        exit(math_ops.less(x, 10))

    def b(x):
        with ops.control_dependencies([x]):
            a = constant_op.constant(np.ones(2000), dtype=dtypes.float32)
            v = gen_data_flow_ops.stack_push(h, a, swap_memory=True)
        with ops.control_dependencies([v]):
            exit(math_ops.add(x, 1))

    r = control_flow_ops.while_loop(c, b, [n])

    v = constant_op.constant(np.zeros(2000), dtype=dtypes.float32)

    def c1(x, y):
        del y
        exit(math_ops.greater(x, 0))

    def b1(x, y):
        nx = math_ops.subtract(x, 1)
        ny = y + gen_data_flow_ops.stack_pop(h, dtypes.float32)
        exit([nx, ny])

    _, ry = control_flow_ops.while_loop(
        c1, b1, [r, v], [r.get_shape(), tensor_shape.unknown_shape()])
    self.assertAllClose(np.ones(2000) * 10.0, self.evaluate(ry))
