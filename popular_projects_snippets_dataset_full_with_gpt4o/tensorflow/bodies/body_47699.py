# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
config = {'padding': self.padding, 'data_format': self.data_format}
base_config = super(ZeroPadding3D, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
