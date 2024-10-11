# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
with self.cached_session():
    init = init_ops.constant_initializer(value, dtype=dtypes.int32)
    x = variable_scope.get_variable(name, shape=shape, initializer=init)
    self.evaluate(x.initializer)

    actual = array_ops.reshape(x, [-1]).eval()
    self.assertEqual(len(actual), len(expected))
    for a, e in zip(actual, expected):
        self.assertEqual(a, e)
