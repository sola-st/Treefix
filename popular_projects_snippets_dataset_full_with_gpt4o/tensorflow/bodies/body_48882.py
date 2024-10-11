# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Returns the config of the layer.

    A layer config is a Python dictionary (serializable)
    containing the configuration of a layer.
    The same layer can be reinstantiated later
    (without its trained weights) from this configuration.

    The config of a layer does not include connectivity
    information, nor the layer class name. These are handled
    by `Network` (one layer of abstraction above).

    Note that `get_config()` does not guarantee to return a fresh copy of dict
    every time it is called. The callers should make a copy of the returned dict
    if they want to modify it.

    Returns:
        Python dictionary.
    """
all_args = tf_inspect.getfullargspec(self.__init__).args
config = {
    'name': self.name,
    'trainable': self.trainable,
}
if hasattr(self, '_batch_input_shape'):
    config['batch_input_shape'] = self._batch_input_shape
config['dtype'] = policy.serialize(self._dtype_policy)
if hasattr(self, 'dynamic'):
    # Only include `dynamic` in the `config` if it is `True`
    if self.dynamic:
        config['dynamic'] = self.dynamic
    elif 'dynamic' in all_args:
        all_args.remove('dynamic')
expected_args = config.keys()
# Finds all arguments in the `__init__` that are not in the config:
extra_args = [arg for arg in all_args if arg not in expected_args]
# Check that either the only argument in the `__init__` is  `self`,
# or that `get_config` has been overridden:
if len(extra_args) > 1 and hasattr(self.get_config, '_is_default'):
    raise NotImplementedError('Layer %s has arguments in `__init__` and '
                              'therefore must override `get_config`.' %
                              self.__class__.__name__)
exit(config)
