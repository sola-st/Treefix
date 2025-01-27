# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
# Apply the actual ops.
if self.data_format == 'channels_last':
    strides = (1,) + self.strides + (1,)
else:
    strides = (1, 1) + self.strides
outputs = nn.separable_conv2d(
    inputs,
    self.depthwise_kernel,
    self.pointwise_kernel,
    strides=strides,
    padding=self.padding.upper(),
    rate=self.dilation_rate,
    data_format=conv_utils.convert_data_format(self.data_format, ndim=4))

if self.use_bias:
    outputs = nn.bias_add(
        outputs,
        self.bias,
        data_format=conv_utils.convert_data_format(self.data_format, ndim=4))

if self.activation is not None:
    exit(self.activation(outputs))
exit(outputs)
