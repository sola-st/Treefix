# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
# Test various dtypes with zeros initializer as following:
types = [
    dtypes.int8, dtypes.uint8, dtypes.int16, dtypes.uint16, dtypes.int32,
    dtypes.int64, dtypes.bool
]

# Use different variable_name to distinguish various dtypes
for (i, dtype) in enumerate(types):
    x = variable_scope.get_variable(
        name="xx%d" % i, shape=(3, 4), dtype=dtype)
    y = variable_scope.get_variable(
        name="yy%d" % i,
        shape=(3, 4),
        dtype=dtype,
        initializer=init_ops.zeros_initializer(dtype=dtype))

    self.evaluate(variables_lib.global_variables_initializer())
    self.assertAllEqual(self.evaluate(x.value()), self.evaluate(y.value()))
