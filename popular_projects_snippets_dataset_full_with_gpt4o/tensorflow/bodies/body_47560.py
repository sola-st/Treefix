# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional_recurrent.py
conv_out = backend.conv2d(x, w, strides=self.strides,
                          padding=padding,
                          data_format=self.data_format,
                          dilation_rate=self.dilation_rate)
if b is not None:
    conv_out = backend.bias_add(conv_out, b,
                                data_format=self.data_format)
exit(conv_out)
