# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
config = {
    'filters':
        self.filters,
    'kernel_size':
        self.kernel_size,
    'strides':
        self.strides,
    'padding':
        self.padding,
    'data_format':
        self.data_format,
    'depth_multiplier':
        self.depth_multiplier,
    'dilation_rate':
        self.dilation_rate,
    'activation':
        activations.serialize(self.activation),
    'use_bias':
        self.use_bias,
    'depthwise_initializer':
        initializers.serialize(self.depthwise_initializer),
    'pointwise_initializer':
        initializers.serialize(self.pointwise_initializer),
    'bias_initializer':
        initializers.serialize(self.bias_initializer),
    'depthwise_regularizer':
        regularizers.serialize(self.depthwise_regularizer),
    'pointwise_regularizer':
        regularizers.serialize(self.pointwise_regularizer),
    'bias_regularizer':
        regularizers.serialize(self.bias_regularizer),
    'activity_regularizer':
        regularizers.serialize(self.activity_regularizer),
    'depthwise_constraint':
        constraints.serialize(self.depthwise_constraint),
    'pointwise_constraint':
        constraints.serialize(self.pointwise_constraint),
    'bias_constraint':
        constraints.serialize(self.bias_constraint)
}
base_config = super(SeparableConv, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
