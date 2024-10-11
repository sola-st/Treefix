# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_d9m_test.py
random_seed.set_seed(seed)
batch_size = 2  # no interaction over batch, so make small
if use_cudnn:
    # When op-determinism is not enabled, one input channel, plus a
    # cuDNN-supported filter size and number of output channels will result
    # in cuDNN being used for both backprop-to-input and backprop-to-filter on
    # cuDNN 7.6.3 and higher. When op-determnism is enabled, cuDNN is always
    # used for backprop-to-filter.
    input_channels = 1
else:
    input_channels = 2  # no interaction over channels, so make small
input_height = 500
input_width = 1000
if data_format == "NHWC":
    input_shape = (batch_size, input_height, input_width, input_channels)
else:  # "NCHW"
    input_shape = (batch_size, input_channels, input_height, input_width)
input_data = random_ops.random_normal(input_shape, dtype=dtype)
# The following filter size results in nondeterminism being exercised in
# cuDNN backprop (when determinism is not enabled) to both input and filter
# as well as in the specialized (non-cuDNN) depthwise backprop to filter.
filter_height = 7
filter_width = 7
channel_multiplier = 10
filter_shape = (filter_height, filter_width, input_channels,
                channel_multiplier)
filter_data = random_ops.random_normal(filter_shape, dtype=dtype)
strides = [1, 1, 1, 1]
padding = "SAME"
output_height = input_height  # because same padding
output_width = input_width  # because same padding
output_channels = input_channels * channel_multiplier
if data_format == "NHWC":
    output_shape = (batch_size, output_height, output_width, output_channels)
else:  # "NCHW"
    output_shape = (batch_size, output_channels, output_height, output_width)
exit((input_data, filter_data, strides, padding, output_shape))
