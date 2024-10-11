# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
super(DepthwiseConv2D, self).__init__(
    filters=None,
    kernel_size=kernel_size,
    strides=strides,
    padding=padding,
    data_format=data_format,
    dilation_rate=dilation_rate,
    activation=activation,
    use_bias=use_bias,
    bias_regularizer=bias_regularizer,
    activity_regularizer=activity_regularizer,
    bias_constraint=bias_constraint,
    **kwargs)
self.depth_multiplier = depth_multiplier
self.depthwise_initializer = initializers.get(depthwise_initializer)
self.depthwise_regularizer = regularizers.get(depthwise_regularizer)
self.depthwise_constraint = constraints.get(depthwise_constraint)
self.bias_initializer = initializers.get(bias_initializer)
