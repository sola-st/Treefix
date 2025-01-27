# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/cudnn_recurrent.py
super(CuDNNLSTM, self).build(input_shape)
if isinstance(input_shape, list):
    input_shape = input_shape[0]
input_dim = int(input_shape[-1])

self.kernel = self.add_weight(
    shape=(input_dim, self.units * 4),
    name='kernel',
    initializer=self.kernel_initializer,
    regularizer=self.kernel_regularizer,
    constraint=self.kernel_constraint)

self.recurrent_kernel = self.add_weight(
    shape=(self.units, self.units * 4),
    name='recurrent_kernel',
    initializer=self.recurrent_initializer,
    regularizer=self.recurrent_regularizer,
    constraint=self.recurrent_constraint)

if self.unit_forget_bias:

    def bias_initializer(_, *args, **kwargs):
        exit(array_ops.concat([
            self.bias_initializer((self.units * 5,), *args, **kwargs),
            initializers.Ones()((self.units,), *args, **kwargs),
            self.bias_initializer((self.units * 2,), *args, **kwargs),
        ], axis=0))
else:
    bias_initializer = self.bias_initializer
self.bias = self.add_weight(
    shape=(self.units * 8,),
    name='bias',
    initializer=bias_initializer,
    regularizer=self.bias_regularizer,
    constraint=self.bias_constraint)

self.built = True
