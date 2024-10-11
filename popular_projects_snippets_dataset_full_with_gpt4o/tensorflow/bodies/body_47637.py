# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
exit([
    conv_utils.conv_output_length(
        length,
        self.kernel_size[i],
        padding=self.padding,
        stride=self.strides[i],
        dilation=self.dilation_rate[i])
    for i, length in enumerate(spatial_input_shape)
])
