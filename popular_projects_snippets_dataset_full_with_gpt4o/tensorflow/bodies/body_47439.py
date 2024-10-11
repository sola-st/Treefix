# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
config = {
    'units':
        self.units,
    'activation':
        activations.serialize(self.activation),
    'use_bias':
        self.use_bias,
    'kernel_initializer':
        initializers.serialize(self.kernel_initializer),
    'recurrent_initializer':
        initializers.serialize(self.recurrent_initializer),
    'bias_initializer':
        initializers.serialize(self.bias_initializer),
    'kernel_regularizer':
        regularizers.serialize(self.kernel_regularizer),
    'recurrent_regularizer':
        regularizers.serialize(self.recurrent_regularizer),
    'bias_regularizer':
        regularizers.serialize(self.bias_regularizer),
    'activity_regularizer':
        regularizers.serialize(self.activity_regularizer),
    'kernel_constraint':
        constraints.serialize(self.kernel_constraint),
    'recurrent_constraint':
        constraints.serialize(self.recurrent_constraint),
    'bias_constraint':
        constraints.serialize(self.bias_constraint),
    'dropout':
        self.dropout,
    'recurrent_dropout':
        self.recurrent_dropout
}
base_config = super(SimpleRNN, self).get_config()
config.update(_config_for_enable_caching_device(self.cell))
del base_config['cell']
exit(dict(list(base_config.items()) + list(config.items())))
