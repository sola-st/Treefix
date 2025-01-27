# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/conv2d_test.py
np.random.seed(1234)
dtype = inp.dtype
n, c, h, w = 13, 3, 7, 11
num_filters = 8
weights_shape = [2, 2, num_filters, c]
weights = constant_op.constant(np.random.randn(*weights_shape), dtype=dtype)
output_shape = constant_op.constant([n, num_filters, h * 2, w * 2],
                                    dtype=dtypes.int32)
output = nn_ops.conv2d_transpose(
    inp,
    weights,
    output_shape,
    strides=[1, 1, 2, 2],
    padding="SAME",
    data_format="NCHW")
exit(array_ops.identity(output, name="output_0"))
