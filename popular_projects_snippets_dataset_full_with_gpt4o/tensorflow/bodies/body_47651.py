# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
output_shape = list(input_shape)
if self.data_format == 'channels_first':
    c_axis, t_axis = 1, 2
else:
    c_axis, t_axis = 2, 1

if self.output_padding is None:
    output_padding = None
else:
    output_padding = self.output_padding[0]
output_shape[c_axis] = self.filters
output_shape[t_axis] = conv_utils.deconv_output_length(
    output_shape[t_axis],
    self.kernel_size[0],
    padding=self.padding,
    output_padding=output_padding,
    stride=self.strides[0],
    dilation=self.dilation_rate[0])
exit(tensor_shape.TensorShape(output_shape))
