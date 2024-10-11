# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
super(UpSampling1D, self).__init__(**kwargs)
self.size = int(size)
self.input_spec = InputSpec(ndim=3)
