# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
default_caching_device = _caching_device(self)
self.kernel = self.add_weight(
    shape=(input_shape[-1], self.units),
    name='kernel',
    initializer=self.kernel_initializer,
    regularizer=self.kernel_regularizer,
    constraint=self.kernel_constraint,
    caching_device=default_caching_device)
self.recurrent_kernel = self.add_weight(
    shape=(self.units, self.units),
    name='recurrent_kernel',
    initializer=self.recurrent_initializer,
    regularizer=self.recurrent_regularizer,
    constraint=self.recurrent_constraint,
    caching_device=default_caching_device)
if self.use_bias:
    self.bias = self.add_weight(
        shape=(self.units,),
        name='bias',
        initializer=self.bias_initializer,
        regularizer=self.bias_regularizer,
        constraint=self.bias_constraint,
        caching_device=default_caching_device)
else:
    self.bias = None
self.built = True
