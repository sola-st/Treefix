# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
config = {'n': self.n}
base_config = super(RepeatVector, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
