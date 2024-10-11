# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
implementation = kwargs.pop('implementation', 1)
if implementation == 0:
    logging.warning('`implementation=0` has been deprecated, '
                    'and now defaults to `implementation=1`.'
                    'Please update your layer call.')
if 'enable_caching_device' in kwargs:
    cell_kwargs = {'enable_caching_device':
                   kwargs.pop('enable_caching_device')}
else:
    cell_kwargs = {}
cell = LSTMCell(
    units,
    activation=activation,
    recurrent_activation=recurrent_activation,
    use_bias=use_bias,
    kernel_initializer=kernel_initializer,
    recurrent_initializer=recurrent_initializer,
    unit_forget_bias=unit_forget_bias,
    bias_initializer=bias_initializer,
    kernel_regularizer=kernel_regularizer,
    recurrent_regularizer=recurrent_regularizer,
    bias_regularizer=bias_regularizer,
    kernel_constraint=kernel_constraint,
    recurrent_constraint=recurrent_constraint,
    bias_constraint=bias_constraint,
    dropout=dropout,
    recurrent_dropout=recurrent_dropout,
    implementation=implementation,
    dtype=kwargs.get('dtype'),
    trainable=kwargs.get('trainable', True),
    **cell_kwargs)
super(LSTM, self).__init__(
    cell,
    return_sequences=return_sequences,
    return_state=return_state,
    go_backwards=go_backwards,
    stateful=stateful,
    unroll=unroll,
    **kwargs)
self.activity_regularizer = regularizers.get(activity_regularizer)
self.input_spec = [InputSpec(ndim=3)]
