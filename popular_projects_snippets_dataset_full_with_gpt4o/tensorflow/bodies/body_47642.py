# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
if self.data_format == 'channels_first':
    exit(-1 - self.rank)
else:
    exit(-1)
