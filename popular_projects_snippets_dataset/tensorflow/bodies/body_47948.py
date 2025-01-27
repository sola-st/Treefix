# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/cudnn_recurrent.py
self.units = units
cell_spec = collections.namedtuple('cell', 'state_size')
self._cell = cell_spec(state_size=self.units)
super(CuDNNGRU, self).__init__(
    return_sequences=return_sequences,
    return_state=return_state,
    go_backwards=go_backwards,
    stateful=stateful,
    **kwargs)

self.kernel_initializer = initializers.get(kernel_initializer)
self.recurrent_initializer = initializers.get(recurrent_initializer)
self.bias_initializer = initializers.get(bias_initializer)

self.kernel_regularizer = regularizers.get(kernel_regularizer)
self.recurrent_regularizer = regularizers.get(recurrent_regularizer)
self.bias_regularizer = regularizers.get(bias_regularizer)
self.activity_regularizer = regularizers.get(activity_regularizer)

self.kernel_constraint = constraints.get(kernel_constraint)
self.recurrent_constraint = constraints.get(recurrent_constraint)
self.bias_constraint = constraints.get(bias_constraint)
