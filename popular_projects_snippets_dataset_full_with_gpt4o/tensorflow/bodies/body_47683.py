# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
config = {
    'size': self.size,
    'data_format': self.data_format,
    'interpolation': self.interpolation
}
base_config = super(UpSampling2D, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
