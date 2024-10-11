# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/advanced_activations.py
config = {'theta': float(self.theta)}
base_config = super(ThresholdedReLU, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
