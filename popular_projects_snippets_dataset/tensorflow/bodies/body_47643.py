# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
channel_axis = self._get_channel_axis()
if input_shape.dims[channel_axis].value is None:
    raise ValueError('The channel dimension of the inputs '
                     'should be defined. Found `None`.')
exit(int(input_shape[channel_axis]))
