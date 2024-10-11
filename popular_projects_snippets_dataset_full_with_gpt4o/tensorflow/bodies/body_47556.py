# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional_recurrent.py
super(ConvLSTM2DCell, self).__init__(**kwargs)
self.filters = filters
self.kernel_size = conv_utils.normalize_tuple(kernel_size, 2, 'kernel_size')
self.strides = conv_utils.normalize_tuple(strides, 2, 'strides')
self.padding = conv_utils.normalize_padding(padding)
self.data_format = conv_utils.normalize_data_format(data_format)
self.dilation_rate = conv_utils.normalize_tuple(dilation_rate, 2,
                                                'dilation_rate')
self.activation = activations.get(activation)
self.recurrent_activation = activations.get(recurrent_activation)
self.use_bias = use_bias

self.kernel_initializer = initializers.get(kernel_initializer)
self.recurrent_initializer = initializers.get(recurrent_initializer)
self.bias_initializer = initializers.get(bias_initializer)
self.unit_forget_bias = unit_forget_bias

self.kernel_regularizer = regularizers.get(kernel_regularizer)
self.recurrent_regularizer = regularizers.get(recurrent_regularizer)
self.bias_regularizer = regularizers.get(bias_regularizer)

self.kernel_constraint = constraints.get(kernel_constraint)
self.recurrent_constraint = constraints.get(recurrent_constraint)
self.bias_constraint = constraints.get(bias_constraint)

self.dropout = min(1., max(0., dropout))
self.recurrent_dropout = min(1., max(0., recurrent_dropout))
self.state_size = (self.filters, self.filters)
