# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
inputs_shape = array_ops.shape(inputs)
batch_size = inputs_shape[0]
if self.data_format == 'channels_first':
    d_axis, h_axis, w_axis = 2, 3, 4
else:
    d_axis, h_axis, w_axis = 1, 2, 3

depth = inputs_shape[d_axis]
height = inputs_shape[h_axis]
width = inputs_shape[w_axis]

kernel_d, kernel_h, kernel_w = self.kernel_size
stride_d, stride_h, stride_w = self.strides

if self.output_padding is None:
    out_pad_d = out_pad_h = out_pad_w = None
else:
    out_pad_d, out_pad_h, out_pad_w = self.output_padding

# Infer the dynamic output shape:
out_depth = conv_utils.deconv_output_length(depth,
                                            kernel_d,
                                            padding=self.padding,
                                            output_padding=out_pad_d,
                                            stride=stride_d)
out_height = conv_utils.deconv_output_length(height,
                                             kernel_h,
                                             padding=self.padding,
                                             output_padding=out_pad_h,
                                             stride=stride_h)
out_width = conv_utils.deconv_output_length(width,
                                            kernel_w,
                                            padding=self.padding,
                                            output_padding=out_pad_w,
                                            stride=stride_w)
if self.data_format == 'channels_first':
    output_shape = (batch_size, self.filters, out_depth, out_height,
                    out_width)
    strides = (1, 1, stride_d, stride_h, stride_w)
else:
    output_shape = (batch_size, out_depth, out_height, out_width,
                    self.filters)
    strides = (1, stride_d, stride_h, stride_w, 1)

output_shape_tensor = array_ops.stack(output_shape)
outputs = nn.conv3d_transpose(
    inputs,
    self.kernel,
    output_shape_tensor,
    strides,
    data_format=conv_utils.convert_data_format(self.data_format, ndim=5),
    padding=self.padding.upper())

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
