# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
if self.padding == 'causal':
    inputs = array_ops.pad(inputs, self._compute_causal_padding(inputs))
if self.data_format == 'channels_last':
    strides = (1,) + self.strides * 2 + (1,)
    spatial_start_dim = 1
else:
    strides = (1, 1) + self.strides * 2
    spatial_start_dim = 2

# Explicitly broadcast inputs and kernels to 4D.
# TODO(fchollet): refactor when a native separable_conv1d op is available.
inputs = array_ops.expand_dims(inputs, spatial_start_dim)
depthwise_kernel = array_ops.expand_dims(self.depthwise_kernel, 0)
pointwise_kernel = array_ops.expand_dims(self.pointwise_kernel, 0)
dilation_rate = (1,) + self.dilation_rate

if self.padding == 'causal':
    op_padding = 'valid'
else:
    op_padding = self.padding
outputs = nn.separable_conv2d(
    inputs,
    depthwise_kernel,
    pointwise_kernel,
    strides=strides,
    padding=op_padding.upper(),
    rate=dilation_rate,
    data_format=conv_utils.convert_data_format(self.data_format, ndim=4))

if self.use_bias:
    outputs = nn.bias_add(
        outputs,
        self.bias,
        data_format=conv_utils.convert_data_format(self.data_format, ndim=4))

outputs = array_ops.squeeze(outputs, [spatial_start_dim])

if self.activation is not None:
    exit(self.activation(outputs))
exit(outputs)
