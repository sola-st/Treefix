# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
super(Conv, self).__init__(
    trainable=trainable,
    name=name,
    activity_regularizer=regularizers.get(activity_regularizer),
    **kwargs)
self.rank = rank

if isinstance(filters, float):
    filters = int(filters)
if filters is not None and filters < 0:
    raise ValueError(f'Received a negative value for `filters`.'
                     f'Was expecting a positive value, got {filters}.')
self.filters = filters
self.groups = groups or 1
self.kernel_size = conv_utils.normalize_tuple(
    kernel_size, rank, 'kernel_size')
self.strides = conv_utils.normalize_tuple(strides, rank, 'strides')
self.padding = conv_utils.normalize_padding(padding)
self.data_format = conv_utils.normalize_data_format(data_format)
self.dilation_rate = conv_utils.normalize_tuple(
    dilation_rate, rank, 'dilation_rate')

self.activation = activations.get(activation)
self.use_bias = use_bias

self.kernel_initializer = initializers.get(kernel_initializer)
self.bias_initializer = initializers.get(bias_initializer)
self.kernel_regularizer = regularizers.get(kernel_regularizer)
self.bias_regularizer = regularizers.get(bias_regularizer)
self.kernel_constraint = constraints.get(kernel_constraint)
self.bias_constraint = constraints.get(bias_constraint)
self.input_spec = InputSpec(min_ndim=self.rank + 2)

self._validate_init()
self._is_causal = self.padding == 'causal'
self._channels_first = self.data_format == 'channels_first'
self._tf_data_format = conv_utils.convert_data_format(
    self.data_format, self.rank + 2)
