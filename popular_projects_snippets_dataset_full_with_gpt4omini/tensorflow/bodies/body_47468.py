# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
exit(backend.concatenate([
    self.bias_initializer((self.units,), *args, **kwargs),
    initializers.get('ones')((self.units,), *args, **kwargs),
    self.bias_initializer((self.units * 2,), *args, **kwargs),
]))
