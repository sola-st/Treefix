# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
config = {'target_shape': self.target_shape}
base_config = super(Reshape, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
