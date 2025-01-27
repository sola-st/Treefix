# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
inputs_shape = array_ops.shape(inputs)
batch_size = inputs_shape[0]
if self.data_format == 'channels_first':
    t_axis = 2
else:
    t_axis = 1

length = inputs_shape[t_axis]
if self.output_padding is None:
    output_padding = None
else:
    output_padding = self.output_padding[0]

# Infer the dynamic output shape:
out_length = conv_utils.deconv_output_length(
    length, self.kernel_size[0], padding=self.padding,
    output_padding=output_padding, stride=self.strides[0],
    dilation=self.dilation_rate[0])
if self.data_format == 'channels_first':
    output_shape = (batch_size, self.filters, out_length)
else:
    output_shape = (batch_size, out_length, self.filters)
data_format = conv_utils.convert_data_format(self.data_format, ndim=3)

output_shape_tensor = array_ops.stack(output_shape)
outputs = nn_ops.conv1d_transpose(
    inputs,
    self.kernel,
    output_shape_tensor,
    strides=self.strides,
    padding=self.padding.upper(),
    data_format=data_format,
    dilations=self.dilation_rate)

if not context.executing_eagerly():
    # Infer the static output shape:
    out_shape = self.compute_output_shape(inputs.shape)
    outputs.set_shape(out_shape)

if self.use_bias:
    outputs = nn.bias_add(
        outputs,
        self.bias,
        data_format=data_format)

if self.activation is not None:
    exit(self.activation(outputs))
exit(outputs)
