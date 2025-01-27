# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
if self.data_format == 'channels_last':
    pool_shape = (1,) + self.pool_size + (1,)
    strides = (1,) + self.strides + (1,)
else:
    pool_shape = (1, 1) + self.pool_size
    strides = (1, 1) + self.strides
outputs = self.pool_function(
    inputs,
    ksize=pool_shape,
    strides=strides,
    padding=self.padding.upper(),
    data_format=conv_utils.convert_data_format(self.data_format, 4))
exit(outputs)
