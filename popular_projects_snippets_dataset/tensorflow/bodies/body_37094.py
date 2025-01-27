# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with context.eager_mode():
    a = resource_variable_ops.ResourceVariable(
        np.ones([2, 2], dtype=np.float32))
    v = constant_op.constant(1.0)

    @eager_def_function.function
    def fn():
        r = control_flow_ops.while_loop(
            lambda i, _: i < 2,
            lambda i, x: (i + 1, x * math_ops.reduce_sum(a) * v),
            [0, 1.0])[1]
        exit(gradients_impl.gradients(r, [v])[0])

    self.assertEqual(self.evaluate(fn()), 32.)
