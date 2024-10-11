# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
input_dim = input_shape[-1]
default_caching_device = _caching_device(self)
self.kernel = self.add_weight(
    shape=(input_dim, self.units * 3),
    name='kernel',
    initializer=self.kernel_initializer,
    regularizer=self.kernel_regularizer,
    constraint=self.kernel_constraint,
    caching_device=default_caching_device)
self.recurrent_kernel = self.add_weight(
    shape=(self.units, self.units * 3),
    name='recurrent_kernel',
    initializer=self.recurrent_initializer,
    regularizer=self.recurrent_regularizer,
    constraint=self.recurrent_constraint,
    caching_device=default_caching_device)

if self.use_bias:
    if not self.reset_after:
        bias_shape = (3 * self.units,)
    else:
        # separate biases for input and recurrent kernels
        # Note: the shape is intentionally different from CuDNNGRU biases
        # `(2 * 3 * self.units,)`, so that we can distinguish the classes
        # when loading and converting saved weights.
        bias_shape = (2, 3 * self.units)
    self.bias = self.add_weight(shape=bias_shape,
                                name='bias',
                                initializer=self.bias_initializer,
                                regularizer=self.bias_regularizer,
                                constraint=self.bias_constraint,
                                caching_device=default_caching_device)
else:
    self.bias = None
self.built = True
