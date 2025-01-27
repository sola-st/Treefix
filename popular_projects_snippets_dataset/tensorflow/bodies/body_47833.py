# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/merge.py
config = {
    'axes': self.axes,
    'normalize': self.normalize,
}
base_config = super(Dot, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
