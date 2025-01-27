# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/advanced_activations.py
config = {'axis': self.axis}
base_config = super(Softmax, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
