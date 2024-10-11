# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv2d_transpose_test.py
# On GPU, this test does try to allocate the output tensor and OOMs.
with test_util.device(use_gpu=False):
    with self.assertRaises((errors.InvalidArgumentError, ValueError)):
        op = nn_ops.conv2d_transpose(
            input=np.ones((2, 2, 2, 2)),
            output_shape=[114078056, 179835296],
            strides=[10],
            filters=[[[[1]]]])
        self.evaluate(op)
