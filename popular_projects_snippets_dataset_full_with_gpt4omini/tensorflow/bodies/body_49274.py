# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
config = {
    'lr': float(backend.get_value(self.lr)),
    'beta_1': float(backend.get_value(self.beta_1)),
    'beta_2': float(backend.get_value(self.beta_2)),
    'decay': float(backend.get_value(self.decay)),
    'epsilon': self.epsilon
}
base_config = super(Adamax, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
