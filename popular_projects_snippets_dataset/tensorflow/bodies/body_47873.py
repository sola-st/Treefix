# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
config = {'activation': activations.serialize(self.activation)}
base_config = super(Activation, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
