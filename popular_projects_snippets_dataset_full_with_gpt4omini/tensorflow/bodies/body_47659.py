# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
input_shape = tensor_shape.TensorShape(input_shape)
if len(input_shape) != 5:
    raise ValueError('Inputs should have rank 5, received input shape:',
                     str(input_shape))
channel_axis = self._get_channel_axis()
if input_shape.dims[channel_axis].value is None:
    raise ValueError('The channel dimension of the inputs '
                     'should be defined, found None: ' + str(input_shape))
input_dim = int(input_shape[channel_axis])
kernel_shape = self.kernel_size + (self.filters, input_dim)
self.input_spec = InputSpec(ndim=5, axes={channel_axis: input_dim})

self.kernel = self.add_weight(
    'kernel',
    shape=kernel_shape,
    initializer=self.kernel_initializer,
    regularizer=self.kernel_regularizer,
    constraint=self.kernel_constraint,
    trainable=True,
    dtype=self.dtype)
if self.use_bias:
    self.bias = self.add_weight(
        'bias',
        shape=(self.filters,),
        initializer=self.bias_initializer,
        regularizer=self.bias_regularizer,
        constraint=self.bias_constraint,
        trainable=True,
        dtype=self.dtype)
else:
    self.bias = None
self.built = True
