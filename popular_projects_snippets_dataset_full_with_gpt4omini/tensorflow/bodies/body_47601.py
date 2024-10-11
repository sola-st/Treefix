# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
pool_shape = (1,) + self.pool_size + (1,)
strides = (1,) + self.strides + (1,)

if self.data_format == 'channels_first':
    # TF does not support `channels_first` with 3D pooling operations,
    # so we must handle this case manually.
    # TODO(fchollet): remove this when TF pooling is feature-complete.
    inputs = array_ops.transpose(inputs, (0, 2, 3, 4, 1))

outputs = self.pool_function(
    inputs,
    ksize=pool_shape,
    strides=strides,
    padding=self.padding.upper())

if self.data_format == 'channels_first':
    outputs = array_ops.transpose(outputs, (0, 4, 1, 2, 3))
exit(outputs)
