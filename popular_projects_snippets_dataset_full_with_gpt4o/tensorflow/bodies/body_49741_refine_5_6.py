self = type('MockSelf', (object,), {})() # pragma: no cover
filters = 32 # pragma: no cover
kernel_size = (3, 3) # pragma: no cover
strides = (2, 2) # pragma: no cover
padding = 'same' # pragma: no cover
data_format = 'channels_last' # pragma: no cover
use_bias = True # pragma: no cover
activity_regularizer = None # pragma: no cover
trainable = True # pragma: no cover
name = 'conv2d_transpose' # pragma: no cover
kwargs = {} # pragma: no cover

self = type('MockSelf', (object,), {})() # pragma: no cover
filters = 64 # pragma: no cover
kernel_size = (3, 3) # pragma: no cover
strides = (2, 2) # pragma: no cover
padding = 'same' # pragma: no cover
data_format = 'channels_last' # pragma: no cover
use_bias = True # pragma: no cover
bias_initializer = 'zeros' # pragma: no cover
bias_regularizer = None # pragma: no cover
activity_regularizer = None # pragma: no cover
bias_constraint = None # pragma: no cover
trainable = True # pragma: no cover
name = 'conv2d_transpose' # pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/convolutional.py
from l3.Runtime import _l_
super(Conv2DTranspose, self).__init__(
    filters=filters,
    kernel_size=kernel_size,
    strides=strides,
    padding=padding,
    data_format=data_format,
    activation=activation,
    use_bias=use_bias,
    kernel_initializer=kernel_initializer,
    bias_initializer=bias_initializer,
    kernel_regularizer=kernel_regularizer,
    bias_regularizer=bias_regularizer,
    activity_regularizer=activity_regularizer,
    kernel_constraint=kernel_constraint,
    bias_constraint=bias_constraint,
    trainable=trainable,
    name=name,
    **kwargs)
_l_(18727)
