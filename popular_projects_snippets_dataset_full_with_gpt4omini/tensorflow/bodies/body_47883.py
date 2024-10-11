# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
super(Flatten, self).__init__(**kwargs)
self.data_format = conv_utils.normalize_data_format(data_format)
self.input_spec = InputSpec(min_ndim=1)
self._channels_first = self.data_format == 'channels_first'
