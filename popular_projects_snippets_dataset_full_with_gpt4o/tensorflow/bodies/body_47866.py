# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
super(SpatialDropout2D, self).__init__(rate, **kwargs)
if data_format is None:
    data_format = K.image_data_format()
if data_format not in {'channels_last', 'channels_first'}:
    raise ValueError('data_format must be in '
                     '{"channels_last", "channels_first"}')
self.data_format = data_format
self.input_spec = InputSpec(ndim=4)
