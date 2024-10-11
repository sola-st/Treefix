# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/dense_attention.py
config = {'use_scale': self.use_scale}
base_config = super(Attention, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
