# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
super(RepeatVector, self).__init__(**kwargs)
self.n = n
if not isinstance(n, int):
    raise TypeError(f'Expected an integer value for `n`, got {type(n)}.')
self.input_spec = InputSpec(ndim=2)
