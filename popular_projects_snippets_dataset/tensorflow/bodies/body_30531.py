# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
with self.session():
    shape = [2, 3]
    x = variable_scope.get_variable(
        "x", shape=shape, initializer=init_ops.ones_initializer())
    self.evaluate(x.initializer)
    self.assertAllEqual(x, np.ones(shape))
