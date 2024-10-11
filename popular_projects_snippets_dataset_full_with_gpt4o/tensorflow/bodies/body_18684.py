# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
with test_util.use_gpu():
    init = init_ops_v2.constant_initializer(value)
    x = init(shape)

    actual = self.evaluate(array_ops.reshape(x, [-1]))
    self.assertEqual(len(actual), len(expected))
    for a, e in zip(actual, expected):
        self.assertEqual(a, e)
