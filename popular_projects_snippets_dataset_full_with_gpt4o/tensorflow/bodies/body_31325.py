# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_conv2d_test.py
with self.session():
    with self.assertRaises((errors.InvalidArgumentError, ValueError)):
        op = nn_ops.atrous_conv2d(
            value=np.ones((1, 1, 1, 5)),
            filters=np.ones((1, 1, 5, 1)),
            rate=2147483647,
            padding="SAME")
        self.evaluate(op)
