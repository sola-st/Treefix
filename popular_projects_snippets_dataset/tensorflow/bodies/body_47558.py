# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional_recurrent.py

if self.data_format == 'channels_first':
    channel_axis = 1
else:
    channel_axis = -1
if input_shape[channel_axis] is None:
    raise ValueError('The channel dimension of the inputs '
                     'should be defined. Found `None`.')
input_dim = input_shape[channel_axis]
kernel_shape = self.kernel_size + (input_dim, self.filters * 4)
self.kernel_shape = kernel_shape
recurrent_kernel_shape = self.kernel_size + (self.filters, self.filters * 4)

self.kernel = self.add_weight(shape=kernel_shape,
                              initializer=self.kernel_initializer,
                              name='kernel',
                              regularizer=self.kernel_regularizer,
                              constraint=self.kernel_constraint)
self.recurrent_kernel = self.add_weight(
    shape=recurrent_kernel_shape,
    initializer=self.recurrent_initializer,
    name='recurrent_kernel',
    regularizer=self.recurrent_regularizer,
    constraint=self.recurrent_constraint)

if self.use_bias:
    if self.unit_forget_bias:

        def bias_initializer(_, *args, **kwargs):
            exit(backend.concatenate([
                self.bias_initializer((self.filters,), *args, **kwargs),
                initializers.get('ones')((self.filters,), *args, **kwargs),
                self.bias_initializer((self.filters * 2,), *args, **kwargs),
            ]))
    else:
        bias_initializer = self.bias_initializer
    self.bias = self.add_weight(
        shape=(self.filters * 4,),
        name='bias',
        initializer=bias_initializer,
        regularizer=self.bias_regularizer,
        constraint=self.bias_constraint)
else:
    self.bias = None
self.built = True
