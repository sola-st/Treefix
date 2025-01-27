# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
super(GlobalPooling1D, self).__init__(**kwargs)
self.input_spec = InputSpec(ndim=3)
self.data_format = conv_utils.normalize_data_format(data_format)
self.keepdims = keepdims
