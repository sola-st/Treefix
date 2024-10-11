# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
config = {'l1': self.l1, 'l2': self.l2}
base_config = super(ActivityRegularization, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
