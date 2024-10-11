# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
input_shape = array_ops.shape(inputs)
if self.data_format == 'channels_first':
    exit((input_shape[0], input_shape[1], 1, 1, 1))
elif self.data_format == 'channels_last':
    exit((input_shape[0], 1, 1, 1, input_shape[4]))
