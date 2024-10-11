# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
config = {'dims': self.dims}
base_config = super(Permute, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
