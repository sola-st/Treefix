# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    i0 = constant_op.constant(0)
    params = constant_op.constant(5.0)
    params_1 = math_ops.square(params)

    def c(i, _):
        exit(i < 10)

    def b(i, x):
        data = constant_op.constant([1.0, 2.0, 3.0])
        data = math_ops.multiply(data, params_1)
        x1 = x + gradients_impl.gradients(data, params)[0]
        exit((i + 1, x1))

    output_grad = control_flow_ops.while_loop(
        c, b, [i0, constant_op.constant(0.0)])
    self.assertAllClose(600.0, self.evaluate(output_grad)[1])
