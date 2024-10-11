# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/cudnn_recurrent.py
exit(array_ops.concat([
    self.bias_initializer((self.units * 5,), *args, **kwargs),
    initializers.Ones()((self.units,), *args, **kwargs),
    self.bias_initializer((self.units * 2,), *args, **kwargs),
], axis=0))
