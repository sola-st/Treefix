# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
config = {
    'rate': self.rate,
    'noise_shape': self.noise_shape,
    'seed': self.seed
}
base_config = super(Dropout, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
