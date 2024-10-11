# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
with self.cached_session():
    x = variables.Variable(5, dtype=dtypes.float32)
    y = variables.Variable(True, dtype=dtypes.bool)
    cast = math_ops.cast(y, x.dtype)
    self.evaluate(variables.global_variables_initializer())
    self.assertEqual(1.0, self.evaluate(cast))
