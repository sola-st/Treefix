# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
config = {'data_format': self.data_format, 'keepdims': self.keepdims}
base_config = super(GlobalPooling1D, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
