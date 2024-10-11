# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
super(Dense, self).__init__(
    activity_regularizer=activity_regularizer, **kwargs)

self.units = int(units) if not isinstance(units, int) else units
if self.units < 0:
    raise ValueError(f'Received an invalid value for `units`, expected '
                     f'a positive integer, got {units}.')
self.activation = activations.get(activation)
self.use_bias = use_bias
self.kernel_initializer = initializers.get(kernel_initializer)
self.bias_initializer = initializers.get(bias_initializer)
self.kernel_regularizer = regularizers.get(kernel_regularizer)
self.bias_regularizer = regularizers.get(bias_regularizer)
self.kernel_constraint = constraints.get(kernel_constraint)
self.bias_constraint = constraints.get(bias_constraint)

self.input_spec = InputSpec(min_ndim=2)
self.supports_masking = True
