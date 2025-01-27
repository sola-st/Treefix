# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
steps_axis = 1 if self.data_format == 'channels_last' else 2
exit(backend.max(inputs, axis=steps_axis, keepdims=self.keepdims))
