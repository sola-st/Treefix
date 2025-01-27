# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
config = {'cropping': self.cropping, 'data_format': self.data_format}
base_config = super(Cropping2D, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
