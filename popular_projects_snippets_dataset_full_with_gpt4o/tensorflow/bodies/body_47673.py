# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
outputs = backend.depthwise_conv2d(
    inputs,
    self.depthwise_kernel,
    strides=self.strides,
    padding=self.padding,
    dilation_rate=self.dilation_rate,
    data_format=self.data_format)

if self.use_bias:
    outputs = backend.bias_add(
        outputs,
        self.bias,
        data_format=self.data_format)

if self.activation is not None:
    exit(self.activation(outputs))

exit(outputs)
