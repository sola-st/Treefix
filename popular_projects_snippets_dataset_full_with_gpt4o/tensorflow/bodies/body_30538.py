# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
with self.cached_session():
    init = init_ops.constant_initializer(value, dtype=dtypes.int32)
    x = variable_scope.get_variable(name, shape=shape, initializer=init)
    self.evaluate(x.initializer)

    actual = array_ops.reshape(x, [-1]).eval()
    self.assertGreater(len(actual), len(expected))
    for i in range(len(actual)):
        a = actual[i]
        e = expected[i] if i < len(expected) else expected[-1]
        self.assertEqual(a, e)
