# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
super(UpSampling2D, self).__init__(**kwargs)
self.data_format = conv_utils.normalize_data_format(data_format)
self.size = conv_utils.normalize_tuple(size, 2, 'size')
if interpolation not in {'nearest', 'bilinear'}:
    raise ValueError('`interpolation` argument should be one of `"nearest"` '
                     'or `"bilinear"`.')
self.interpolation = interpolation
self.input_spec = InputSpec(ndim=4)
