# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/convolutional.py
super(Conv3DTranspose, self).__init__(
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
