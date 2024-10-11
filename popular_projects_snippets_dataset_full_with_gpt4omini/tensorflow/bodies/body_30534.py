# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
with self.session():
    shape = [2, 3]
    x = variable_scope.get_variable(
        "x",
        shape=shape,
        dtype=dtypes.int32,
        initializer=init_ops.constant_initializer(7))
    self.evaluate(x.initializer)
    self.assertEqual(x.dtype.base_dtype, dtypes.int32)
    self.assertAllEqual(x, 7 * np.ones(shape, dtype=np.int32))
