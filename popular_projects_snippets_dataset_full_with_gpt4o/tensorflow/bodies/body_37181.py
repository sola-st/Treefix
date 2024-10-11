# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    param = constant_op.constant(2.0)
    n0 = constant_op.constant(0)
    y0 = constant_op.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], name="elems")

    def c(i, _):
        exit(i < 10)

    def b(i, y):
        exit([
            i + 1,
            map_fn.map_fn(lambda x: math_ops.multiply(x, param), y)
        ])

    r = control_flow_ops.while_loop(c, b, [n0, y0], parallel_iterations=1)
    r = gradients_impl.gradients(r, param)[0]
    self.assertAllClose(107520.0, self.evaluate(r))
