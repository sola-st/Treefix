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
    'dilation_rate':
        self.dilation_rate,
    'groups':
        self.groups,
    'activation':
        activations.serialize(self.activation),
    'use_bias':
        self.use_bias,
    'kernel_initializer':
        initializers.serialize(self.kernel_initializer),
    'bias_initializer':
        initializers.serialize(self.bias_initializer),
    'kernel_regularizer':
        regularizers.serialize(self.kernel_regularizer),
    'bias_regularizer':
        regularizers.serialize(self.bias_regularizer),
    'activity_regularizer':
        regularizers.serialize(self.activity_regularizer),
    'kernel_constraint':
        constraints.serialize(self.kernel_constraint),
    'bias_constraint':
        constraints.serialize(self.bias_constraint)
}
base_config = super(Conv, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
