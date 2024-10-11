# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Initializes the wrapper Layer for this module.

    Args:
      module: The `tf.Module` instance to be wrapped.
      method_name: (Optional) str. The name of the method to use as the forward
        pass of the module. If not set, defaults to '__call__' if defined, or
        'call'.
      **kwargs: Additional keywrod arguments. See `tf.keras.layers.Layer`.

    Raises:
      ValueError: If `method` is not defined on `module`.
    """
super(ModuleWrapper, self).__init__(**kwargs)
if method_name is None:
    if hasattr(module, '__call__'):
        method_name = '__call__'
    elif hasattr(module, 'call'):
        method_name = 'call'
if method_name is None or not hasattr(module, method_name):
    raise ValueError('{} is not defined on object {}'.format(
        method_name, module))

self._module = module
self._method_name = method_name

# Check if module.__call__ has a `training` arg or accepts `**kwargs`.
method = getattr(module, method_name)
method_arg_spec = tf_inspect.getfullargspec(method)
self._expects_training_arg = ('training' in method_arg_spec.args or
                              method_arg_spec.varkw is not None)
self._expects_mask_arg = ('mask' in method_arg_spec.args or
                          method_arg_spec.varkw is not None)
