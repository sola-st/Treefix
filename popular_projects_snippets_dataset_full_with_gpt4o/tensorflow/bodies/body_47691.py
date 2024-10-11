# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
config = {'padding': self.padding}
base_config = super(ZeroPadding1D, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
