# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
inputs_shape = array_ops.shape(inputs)
batch_size = inputs_shape[0]
if self.data_format == 'channels_first':
    h_axis, w_axis = 2, 3
else:
    h_axis, w_axis = 1, 2

# Use the constant height and weight when possible.
# TODO(scottzhu): Extract this into a utility function that can be applied
# to all convolutional layers, which currently lost the static shape
# information due to tf.shape().
height, width = None, None
if inputs.shape.rank is not None:
    dims = inputs.shape.as_list()
    height = dims[h_axis]
    width = dims[w_axis]
height = height if height is not None else inputs_shape[h_axis]
width = width if width is not None else inputs_shape[w_axis]

kernel_h, kernel_w = self.kernel_size
stride_h, stride_w = self.strides

if self.output_padding is None:
    out_pad_h = out_pad_w = None
else:
    out_pad_h, out_pad_w = self.output_padding

# Infer the dynamic output shape:
out_height = conv_utils.deconv_output_length(height,
                                             kernel_h,
                                             padding=self.padding,
                                             output_padding=out_pad_h,
                                             stride=stride_h,
                                             dilation=self.dilation_rate[0])
out_width = conv_utils.deconv_output_length(width,
                                            kernel_w,
                                            padding=self.padding,
                                            output_padding=out_pad_w,
                                            stride=stride_w,
                                            dilation=self.dilation_rate[1])
if self.data_format == 'channels_first':
    output_shape = (batch_size, self.filters, out_height, out_width)
else:
    output_shape = (batch_size, out_height, out_width, self.filters)

output_shape_tensor = array_ops.stack(output_shape)
outputs = backend.conv2d_transpose(
    inputs,
    self.kernel,
    output_shape_tensor,
    strides=self.strides,
    padding=self.padding,
    data_format=self.data_format,
    dilation_rate=self.dilation_rate)

if not context.executing_eagerly():
    # Infer the static output shape:
    out_shape = self.compute_output_shape(inputs.shape)
    outputs.set_shape(out_shape)

if self.use_bias:
    outputs = nn.bias_add(
        outputs,
        self.bias,
        data_format=conv_utils.convert_data_format(self.data_format, ndim=4))

if self.activation is not None:
    exit(self.activation(outputs))
exit(outputs)
