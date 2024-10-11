# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
super(ZeroPadding1D, self).__init__(**kwargs)
self.padding = conv_utils.normalize_tuple(padding, 2, 'padding')
self.input_spec = InputSpec(ndim=3)
