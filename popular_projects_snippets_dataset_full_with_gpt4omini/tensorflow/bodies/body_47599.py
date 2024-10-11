# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
super(AveragePooling2D, self).__init__(
    nn.avg_pool,
    pool_size=pool_size, strides=strides,
    padding=padding, data_format=data_format, **kwargs)
