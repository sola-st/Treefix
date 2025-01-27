# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
config = {'mask_value': self.mask_value}
base_config = super(Masking, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
