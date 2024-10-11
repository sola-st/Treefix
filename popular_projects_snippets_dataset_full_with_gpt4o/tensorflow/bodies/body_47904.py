# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
dtype = dtypes.as_dtype(self.dtype or K.floatx())
if not (dtype.is_floating or dtype.is_complex):
    raise TypeError('Unable to build `Dense` layer with non-floating point '
                    'dtype %s' % (dtype,))

input_shape = tensor_shape.TensorShape(input_shape)
last_dim = tensor_shape.dimension_value(input_shape[-1])
if last_dim is None:
    raise ValueError('The last dimension of the inputs to `Dense` '
                     'should be defined. Found `None`.')
self.input_spec = InputSpec(min_ndim=2, axes={-1: last_dim})
self.kernel = self.add_weight(
    'kernel',
    shape=[last_dim, self.units],
    initializer=self.kernel_initializer,
    regularizer=self.kernel_regularizer,
    constraint=self.kernel_constraint,
    dtype=self.dtype,
    trainable=True)
if self.use_bias:
    self.bias = self.add_weight(
        'bias',
        shape=[self.units,],
        initializer=self.bias_initializer,
        regularizer=self.bias_regularizer,
        constraint=self.bias_constraint,
        dtype=self.dtype,
        trainable=True)
else:
    self.bias = None
self.built = True
