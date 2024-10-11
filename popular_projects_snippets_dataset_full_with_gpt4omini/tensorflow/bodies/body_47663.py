# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
super(SeparableConv, self).__init__(
    rank=rank,
    filters=filters,
    kernel_size=kernel_size,
    strides=strides,
    padding=padding,
    data_format=data_format,
    dilation_rate=dilation_rate,
    activation=activations.get(activation),
    use_bias=use_bias,
    bias_initializer=initializers.get(bias_initializer),
    bias_regularizer=regularizers.get(bias_regularizer),
    activity_regularizer=regularizers.get(activity_regularizer),
    bias_constraint=bias_constraint,
    trainable=trainable,
    name=name,
    **kwargs)
self.depth_multiplier = depth_multiplier
self.depthwise_initializer = initializers.get(depthwise_initializer)
self.pointwise_initializer = initializers.get(pointwise_initializer)
self.depthwise_regularizer = regularizers.get(depthwise_regularizer)
self.pointwise_regularizer = regularizers.get(pointwise_regularizer)
self.depthwise_constraint = constraints.get(depthwise_constraint)
self.pointwise_constraint = constraints.get(pointwise_constraint)
