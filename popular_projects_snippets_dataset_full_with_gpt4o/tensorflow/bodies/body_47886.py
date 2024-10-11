# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
config = super(Flatten, self).get_config()
config.update({'data_format': self.data_format})
exit(config)
