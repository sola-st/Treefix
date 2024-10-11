# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
config = {
    'lr': float(backend.get_value(self.lr)),
    'rho': self.rho,
    'decay': float(backend.get_value(self.decay)),
    'epsilon': self.epsilon
}
base_config = super(Adadelta, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
