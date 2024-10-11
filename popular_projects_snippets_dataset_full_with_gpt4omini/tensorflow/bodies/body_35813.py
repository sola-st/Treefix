# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
value = [[-42], [133.7]]
shape = [2, 1]
with self.cached_session():
    initializer = lambda: constant_op.constant(value)

    v1 = variables.Variable(initializer, dtype=dtypes.float32)
    self.assertEqual(shape, v1.get_shape())
    self.assertEqual(shape, v1.shape)
    self.assertAllClose(value, self.evaluate(v1.initial_value))
    with self.assertRaises(errors_impl.FailedPreconditionError):
        self.evaluate(v1)

    v2 = variables.Variable(
        math_ops.negative(v1.initialized_value()), dtype=dtypes.float32)
    self.assertEqual(v1.get_shape(), v2.get_shape())
    self.assertEqual(v1.shape, v2.shape)
    self.assertAllClose(np.negative(value), self.evaluate(v2.initial_value))

    with self.assertRaises(errors_impl.FailedPreconditionError):
        self.evaluate(v2)
    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose(np.negative(value), self.evaluate(v2))
