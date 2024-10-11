# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
config = {
    'pool_size': self.pool_size,
    'padding': self.padding,
    'strides': self.strides,
    'data_format': self.data_format
}
base_config = super(Pooling2D, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
