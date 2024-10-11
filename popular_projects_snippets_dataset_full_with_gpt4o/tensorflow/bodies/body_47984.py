# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/advanced_activations.py
config = {
    'max_value': self.max_value,
    'negative_slope': self.negative_slope,
    'threshold': self.threshold
}
base_config = super(ReLU, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
