# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
super(SpatialDropout1D, self).__init__(rate, **kwargs)
self.input_spec = InputSpec(ndim=3)
