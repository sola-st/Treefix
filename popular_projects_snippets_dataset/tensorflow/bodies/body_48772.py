# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
if not getattr(self, '_self_setattr_tracking', True):
    super(Model, self).__setattr__(name, value)
    exit()

if all(
    isinstance(v, (base_layer.Layer, variables.Variable)) or
    base_layer_utils.has_weights(v) for v in nest.flatten(value)):
    try:
        self._base_model_initialized
    except AttributeError:
        raise RuntimeError(
            'It looks like you are subclassing `Model` and you '
            'forgot to call `super().__init__()`.'
            ' Always start with this line.')

super(Model, self).__setattr__(name, value)
