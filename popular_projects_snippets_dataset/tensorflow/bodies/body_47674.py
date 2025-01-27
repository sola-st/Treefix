# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
if self.data_format == 'channels_first':
    rows = input_shape[2]
    cols = input_shape[3]
    out_filters = input_shape[1] * self.depth_multiplier
elif self.data_format == 'channels_last':
    rows = input_shape[1]
    cols = input_shape[2]
    out_filters = input_shape[3] * self.depth_multiplier

rows = conv_utils.conv_output_length(rows, self.kernel_size[0],
                                     self.padding,
                                     self.strides[0],
                                     self.dilation_rate[0])
cols = conv_utils.conv_output_length(cols, self.kernel_size[1],
                                     self.padding,
                                     self.strides[1],
                                     self.dilation_rate[1])
if self.data_format == 'channels_first':
    exit((input_shape[0], out_filters, rows, cols))
elif self.data_format == 'channels_last':
    exit((input_shape[0], rows, cols, out_filters))
