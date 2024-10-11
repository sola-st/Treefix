# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
super(AveragePooling1D, self).__init__(
    functools.partial(backend.pool2d, pool_mode='avg'),
    pool_size=pool_size,
    strides=strides,
    padding=padding,
    data_format=data_format,
    **kwargs)
