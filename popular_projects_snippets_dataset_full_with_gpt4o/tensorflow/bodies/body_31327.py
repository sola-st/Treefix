# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_conv2d_test.py
with self.session():
    with self.assertRaises((errors.InvalidArgumentError, ValueError)):
        op = nn_ops.atrous_conv2d_transpose(
            value=np.ones((10, 1, 1, 1)),
            filters=np.ones((1, 1, 1, 1)),
            rate=1356819205,
            padding="SAME",
            output_shape=[1, 1, 1, 1])
        self.evaluate(op)
