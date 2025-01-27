# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
output_shape = list(input_shape)
if self.data_format == 'channels_first':
    c_axis, d_axis, h_axis, w_axis = 1, 2, 3, 4
else:
    c_axis, d_axis, h_axis, w_axis = 4, 1, 2, 3

kernel_d, kernel_h, kernel_w = self.kernel_size
stride_d, stride_h, stride_w = self.strides

if self.output_padding is None:
    out_pad_d = out_pad_h = out_pad_w = None
else:
    out_pad_d, out_pad_h, out_pad_w = self.output_padding

output_shape[c_axis] = self.filters
output_shape[d_axis] = conv_utils.deconv_output_length(
    output_shape[d_axis],
    kernel_d,
    padding=self.padding,
    output_padding=out_pad_d,
    stride=stride_d)
output_shape[h_axis] = conv_utils.deconv_output_length(
    output_shape[h_axis],
    kernel_h,
    padding=self.padding,
    output_padding=out_pad_h,
    stride=stride_h)
output_shape[w_axis] = conv_utils.deconv_output_length(
    output_shape[w_axis],
    kernel_w,
    padding=self.padding,
    output_padding=out_pad_w,
    stride=stride_w)
exit(tensor_shape.TensorShape(output_shape))
