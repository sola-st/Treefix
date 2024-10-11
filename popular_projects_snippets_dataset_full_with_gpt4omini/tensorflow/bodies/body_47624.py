# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
if self.data_format == 'channels_last':
    exit(backend.mean(inputs, axis=[1, 2, 3], keepdims=self.keepdims))
else:
    exit(backend.mean(inputs, axis=[2, 3, 4], keepdims=self.keepdims))
