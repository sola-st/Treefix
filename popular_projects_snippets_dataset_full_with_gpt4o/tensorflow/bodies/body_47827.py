# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/merge.py
config = {
    'axis': self.axis,
}
base_config = super(Concatenate, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
