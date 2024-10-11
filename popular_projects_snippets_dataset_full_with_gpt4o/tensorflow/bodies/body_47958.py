# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/cudnn_recurrent.py
config = {
    'units': self.units,
    'kernel_initializer': initializers.serialize(self.kernel_initializer),
    'recurrent_initializer':
        initializers.serialize(self.recurrent_initializer),
    'bias_initializer': initializers.serialize(self.bias_initializer),
    'unit_forget_bias': self.unit_forget_bias,
    'kernel_regularizer': regularizers.serialize(self.kernel_regularizer),
    'recurrent_regularizer':
        regularizers.serialize(self.recurrent_regularizer),
    'bias_regularizer': regularizers.serialize(self.bias_regularizer),
    'activity_regularizer':
        regularizers.serialize(self.activity_regularizer),
    'kernel_constraint': constraints.serialize(self.kernel_constraint),
    'recurrent_constraint':
        constraints.serialize(self.recurrent_constraint),
    'bias_constraint': constraints.serialize(self.bias_constraint)
}
base_config = super(CuDNNLSTM, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
