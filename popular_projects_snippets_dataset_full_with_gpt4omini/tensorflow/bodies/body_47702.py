# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
if self.cropping[1] == 0:
    exit(inputs[:, self.cropping[0]:, :])
else:
    exit(inputs[:, self.cropping[0]:-self.cropping[1], :])
