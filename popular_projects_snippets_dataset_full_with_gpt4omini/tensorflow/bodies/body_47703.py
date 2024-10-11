# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
config = {'cropping': self.cropping}
base_config = super(Cropping1D, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
