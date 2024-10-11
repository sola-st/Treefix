# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
config = {
    'lr': float(backend.get_value(self.lr)),
    'momentum': float(backend.get_value(self.momentum)),
    'decay': float(backend.get_value(self.decay)),
    'nesterov': self.nesterov
}
base_config = super(SGD, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
