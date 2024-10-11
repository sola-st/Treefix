# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
with self.session():
    shape = [3]
    x = variable_scope.get_variable(
        "x",
        shape=shape,
        dtype=dtypes.int32,
        initializer=init_ops.constant_initializer((10, 20, 30)))
    self.evaluate(x.initializer)
    self.assertEqual(x.dtype.base_dtype, dtypes.int32)
    self.assertAllEqual(x, [10, 20, 30])
