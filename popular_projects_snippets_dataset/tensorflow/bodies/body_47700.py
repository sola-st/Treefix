# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
super(Cropping1D, self).__init__(**kwargs)
self.cropping = conv_utils.normalize_tuple(cropping, 2, 'cropping')
self.input_spec = InputSpec(ndim=3)
