# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/pooling.py
if strides is None:
    raise ValueError('Argument `strides` must not be None.')
super(MaxPooling3D, self).__init__(
    pool_size=pool_size, strides=strides,
    padding=padding, data_format=data_format, name=name, **kwargs)
