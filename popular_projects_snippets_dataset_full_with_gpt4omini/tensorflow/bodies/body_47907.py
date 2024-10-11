# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
config = super(Dense, self).get_config()
config.update({
    'units': self.units,
    'activation': activations.serialize(self.activation),
    'use_bias': self.use_bias,
    'kernel_initializer': initializers.serialize(self.kernel_initializer),
    'bias_initializer': initializers.serialize(self.bias_initializer),
    'kernel_regularizer': regularizers.serialize(self.kernel_regularizer),
    'bias_regularizer': regularizers.serialize(self.bias_regularizer),
    'activity_regularizer':
        regularizers.serialize(self.activity_regularizer),
    'kernel_constraint': constraints.serialize(self.kernel_constraint),
    'bias_constraint': constraints.serialize(self.bias_constraint)
})
exit(config)
