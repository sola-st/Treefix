# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
super(GlobalPooling2D, self).__init__(**kwargs)
self.data_format = conv_utils.normalize_data_format(data_format)
self.input_spec = InputSpec(ndim=4)
self.keepdims = keepdims
