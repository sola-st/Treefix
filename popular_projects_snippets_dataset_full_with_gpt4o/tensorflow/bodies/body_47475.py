# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
warnings.warn('`tf.keras.experimental.PeepholeLSTMCell` is deprecated '
              'and will be removed in a future version. '
              'Please use tensorflow_addons.rnn.PeepholeLSTMCell '
              'instead.')
super(PeepholeLSTMCell, self).__init__(
    units=units,
    activation=activation,
    recurrent_activation=recurrent_activation,
    use_bias=use_bias,
    kernel_initializer=kernel_initializer,
    recurrent_initializer=recurrent_initializer,
    bias_initializer=bias_initializer,
    unit_forget_bias=unit_forget_bias,
    kernel_regularizer=kernel_regularizer,
    recurrent_regularizer=recurrent_regularizer,
    bias_regularizer=bias_regularizer,
    kernel_constraint=kernel_constraint,
    recurrent_constraint=recurrent_constraint,
    bias_constraint=bias_constraint,
    dropout=dropout,
    recurrent_dropout=recurrent_dropout,
    implementation=kwargs.pop('implementation', 1),
    **kwargs)
