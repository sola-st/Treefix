# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
super(Conv3DTranspose, self).__init__(
    filters=filters,
    kernel_size=kernel_size,
    strides=strides,
    padding=padding,
    data_format=data_format,
    dilation_rate=dilation_rate,
    activation=activations.get(activation),
    use_bias=use_bias,
    kernel_initializer=initializers.get(kernel_initializer),
    bias_initializer=initializers.get(bias_initializer),
    kernel_regularizer=regularizers.get(kernel_regularizer),
    bias_regularizer=regularizers.get(bias_regularizer),
    activity_regularizer=regularizers.get(activity_regularizer),
    kernel_constraint=constraints.get(kernel_constraint),
    bias_constraint=constraints.get(bias_constraint),
    **kwargs)

self.output_padding = output_padding
if self.output_padding is not None:
    self.output_padding = conv_utils.normalize_tuple(
        self.output_padding, 3, 'output_padding')
    for stride, out_pad in zip(self.strides, self.output_padding):
        if out_pad >= stride:
            raise ValueError('Stride ' + str(self.strides) + ' must be '
                             'greater than output padding ' +
                             str(self.output_padding))
