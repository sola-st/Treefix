# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
shape = [0, 2]
with self.cached_session():
    x = variable_scope.get_variable(
        "x",
        shape=shape,
        initializer=init_ops.uniform_unit_scaling_initializer())
    self.evaluate(variables.global_variables_initializer())
    self.assertAllEqual(shape, self.evaluate(x).shape)
