# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
self.data_format = conv_utils.normalize_data_format(data_format)
self.size = conv_utils.normalize_tuple(size, 3, 'size')
self.input_spec = InputSpec(ndim=5)
super(UpSampling3D, self).__init__(**kwargs)
