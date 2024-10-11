# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
if len(input_shape) < 4:
    raise ValueError('Inputs to `DepthwiseConv2D` should have rank 4. '
                     'Received input shape:', str(input_shape))
input_shape = tensor_shape.TensorShape(input_shape)
channel_axis = self._get_channel_axis()
if input_shape.dims[channel_axis].value is None:
    raise ValueError('The channel dimension of the inputs to '
                     '`DepthwiseConv2D` '
                     'should be defined. Found `None`.')
input_dim = int(input_shape[channel_axis])
depthwise_kernel_shape = (self.kernel_size[0],
                          self.kernel_size[1],
                          input_dim,
                          self.depth_multiplier)

self.depthwise_kernel = self.add_weight(
    shape=depthwise_kernel_shape,
    initializer=self.depthwise_initializer,
    name='depthwise_kernel',
    regularizer=self.depthwise_regularizer,
    constraint=self.depthwise_constraint)

if self.use_bias:
    self.bias = self.add_weight(shape=(input_dim * self.depth_multiplier,),
                                initializer=self.bias_initializer,
                                name='bias',
                                regularizer=self.bias_regularizer,
                                constraint=self.bias_constraint)
else:
    self.bias = None
# Set input spec.
self.input_spec = InputSpec(ndim=4, axes={channel_axis: input_dim})
self.built = True
