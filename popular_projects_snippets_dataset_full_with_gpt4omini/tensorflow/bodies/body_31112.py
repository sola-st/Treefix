# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv2d_transpose_test.py
with self.session():
    with self.assertRaises((errors.InvalidArgumentError, ValueError)):
        op = nn_ops.conv2d_transpose(
            input=np.ones((1, 1, 1, 1)),
            filters=np.ones((1, 1, 1, 1)),
            output_shape=[2, -2],
            strides=[1])
        self.evaluate(op)
