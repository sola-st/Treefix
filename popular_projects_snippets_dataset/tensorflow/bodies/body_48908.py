# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
for v in nest.flatten(value):
    if v is not None and not isinstance(v, InputSpec):
        raise TypeError('Layer input_spec must be an instance of InputSpec. '
                        'Got: {}'.format(v))
self._input_spec = value
