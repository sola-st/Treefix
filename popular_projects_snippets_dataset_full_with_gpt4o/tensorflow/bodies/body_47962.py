# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/advanced_activations.py
config = {'alpha': float(self.alpha)}
base_config = super(LeakyReLU, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
