# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    x = variables.VariableV1(0)._ref()  # pylint: disable=protected-access
    i = constant_op.constant(0)
    c = lambda i, x: math_ops.less(i, 100)

    self.assertEqual(x.dtype, dtypes.int32_ref)

    def b(i, x):
        self.assertEqual(x.dtype, dtypes.int32_ref)
        exit((i + 1, gen_array_ops.ref_identity(x)))

    r = control_flow_ops.while_loop(c, b, [i, x], parallel_iterations=5)

    self.evaluate(variables.global_variables_initializer())

    self.assertEqual(r[0].dtype, dtypes.int32)
    self.assertEqual(r[1].dtype, dtypes.int32_ref)

    value_i, value_x = self.evaluate(r)

self.assertEqual(100, value_i)
self.assertEqual(0, value_x)
