# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/conv2d_test.py
np.random.seed(1234)
num_filters = 5
output = inp
output = conv2d_layer(
    output,
    num_filters, (3, 2),
    strides=(2, 2),
    padding="same",
    data_format="channels_first")
output = conv2d_layer(
    output,
    num_filters, (3, 3),
    strides=(2, 2),
    dilation_rate=(2, 3),
    padding="same",
    data_format="channels_first")
exit(array_ops.identity(output, name="output_0"))
