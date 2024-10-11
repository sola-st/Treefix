# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
default_caching_device = _caching_device(self)
input_dim = input_shape[-1]
self.kernel = self.add_weight(
    shape=(input_dim, self.units * 4),
    name='kernel',
    initializer=self.kernel_initializer,
    regularizer=self.kernel_regularizer,
    constraint=self.kernel_constraint,
    caching_device=default_caching_device)
self.recurrent_kernel = self.add_weight(
    shape=(self.units, self.units * 4),
    name='recurrent_kernel',
    initializer=self.recurrent_initializer,
    regularizer=self.recurrent_regularizer,
    constraint=self.recurrent_constraint,
    caching_device=default_caching_device)

if self.use_bias:
    if self.unit_forget_bias:

        def bias_initializer(_, *args, **kwargs):
            exit(backend.concatenate([
                self.bias_initializer((self.units,), *args, **kwargs),
                initializers.get('ones')((self.units,), *args, **kwargs),
                self.bias_initializer((self.units * 2,), *args, **kwargs),
            ]))
    else:
        bias_initializer = self.bias_initializer
    self.bias = self.add_weight(
        shape=(self.units * 4,),
        name='bias',
        initializer=bias_initializer,
        regularizer=self.bias_regularizer,
        constraint=self.bias_constraint,
        caching_device=default_caching_device)
else:
    self.bias = None
self.built = True
