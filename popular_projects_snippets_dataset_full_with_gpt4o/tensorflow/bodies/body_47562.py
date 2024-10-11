# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional_recurrent.py
config = {'filters': self.filters,
          'kernel_size': self.kernel_size,
          'strides': self.strides,
          'padding': self.padding,
          'data_format': self.data_format,
          'dilation_rate': self.dilation_rate,
          'activation': activations.serialize(self.activation),
          'recurrent_activation': activations.serialize(
              self.recurrent_activation),
          'use_bias': self.use_bias,
          'kernel_initializer': initializers.serialize(
              self.kernel_initializer),
          'recurrent_initializer': initializers.serialize(
              self.recurrent_initializer),
          'bias_initializer': initializers.serialize(self.bias_initializer),
          'unit_forget_bias': self.unit_forget_bias,
          'kernel_regularizer': regularizers.serialize(
              self.kernel_regularizer),
          'recurrent_regularizer': regularizers.serialize(
              self.recurrent_regularizer),
          'bias_regularizer': regularizers.serialize(self.bias_regularizer),
          'kernel_constraint': constraints.serialize(
              self.kernel_constraint),
          'recurrent_constraint': constraints.serialize(
              self.recurrent_constraint),
          'bias_constraint': constraints.serialize(self.bias_constraint),
          'dropout': self.dropout,
          'recurrent_dropout': self.recurrent_dropout}
base_config = super(ConvLSTM2DCell, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
