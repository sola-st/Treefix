# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
if units < 0:
    raise ValueError(f'Received an invalid value for units, expected '
                     f'a positive integer, got {units}.')
# By default use cached variable under v2 mode, see b/143699808.
if ops.executing_eagerly_outside_functions():
    self._enable_caching_device = kwargs.pop('enable_caching_device', True)
else:
    self._enable_caching_device = kwargs.pop('enable_caching_device', False)
super(GRUCell, self).__init__(**kwargs)
self.units = units
self.activation = activations.get(activation)
self.recurrent_activation = activations.get(recurrent_activation)
self.use_bias = use_bias

self.kernel_initializer = initializers.get(kernel_initializer)
self.recurrent_initializer = initializers.get(recurrent_initializer)
self.bias_initializer = initializers.get(bias_initializer)

self.kernel_regularizer = regularizers.get(kernel_regularizer)
self.recurrent_regularizer = regularizers.get(recurrent_regularizer)
self.bias_regularizer = regularizers.get(bias_regularizer)

self.kernel_constraint = constraints.get(kernel_constraint)
self.recurrent_constraint = constraints.get(recurrent_constraint)
self.bias_constraint = constraints.get(bias_constraint)

self.dropout = min(1., max(0., dropout))
self.recurrent_dropout = min(1., max(0., recurrent_dropout))

implementation = kwargs.pop('implementation', 1)
if self.recurrent_dropout != 0 and implementation != 1:
    logging.debug(RECURRENT_DROPOUT_WARNING_MSG)
    self.implementation = 1
else:
    self.implementation = implementation
self.reset_after = reset_after
self.state_size = self.units
self.output_size = self.units
