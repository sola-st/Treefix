# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
input_shape = tensor_shape.TensorShape(input_shape)
channel_axis = self._get_channel_axis()
if input_shape.dims[channel_axis].value is None:
    raise ValueError('The channel dimension of the inputs '
                     'should be defined. Found `None`.')
input_dim = int(input_shape[channel_axis])
self.input_spec = InputSpec(ndim=self.rank + 2,
                            axes={channel_axis: input_dim})
depthwise_kernel_shape = self.kernel_size + (input_dim,
                                             self.depth_multiplier)
pointwise_kernel_shape = (
    1,) * self.rank + (self.depth_multiplier * input_dim, self.filters)

self.depthwise_kernel = self.add_weight(
    name='depthwise_kernel',
    shape=depthwise_kernel_shape,
    initializer=self.depthwise_initializer,
    regularizer=self.depthwise_regularizer,
    constraint=self.depthwise_constraint,
    trainable=True,
    dtype=self.dtype)
self.pointwise_kernel = self.add_weight(
    name='pointwise_kernel',
    shape=pointwise_kernel_shape,
    initializer=self.pointwise_initializer,
    regularizer=self.pointwise_regularizer,
    constraint=self.pointwise_constraint,
    trainable=True,
    dtype=self.dtype)
if self.use_bias:
    self.bias = self.add_weight(
        name='bias',
        shape=(self.filters,),
        initializer=self.bias_initializer,
        regularizer=self.bias_regularizer,
        constraint=self.bias_constraint,
        trainable=True,
        dtype=self.dtype)
else:
    self.bias = None
self.built = True
