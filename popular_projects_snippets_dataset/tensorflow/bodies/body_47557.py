# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional_recurrent.py
exit(backend.concatenate([
    self.bias_initializer((self.filters,), *args, **kwargs),
    initializers.get('ones')((self.filters,), *args, **kwargs),
    self.bias_initializer((self.filters * 2,), *args, **kwargs),
]))
