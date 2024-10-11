# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_convolution_test.py
x = array_ops.placeholder(dtypes.float32, [1, 10, None, None])
w = array_ops.zeros([3, 3, 10, 20])
y = nn_ops.convolution(
    x, w, "VALID", dilation_rate=[2, 2], data_format="NCHW")
self.assertEqual(y.shape.as_list(), [1, 20, None, None])
