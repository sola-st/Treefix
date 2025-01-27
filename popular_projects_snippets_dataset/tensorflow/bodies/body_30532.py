# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
with self.session():
    shape = [2, 3]
    x = variable_scope.get_variable(
        "x", shape=shape, initializer=init_ops.constant_initializer(0.0))
    self.evaluate(x.initializer)
    self.assertAllEqual(x, np.zeros(shape))
