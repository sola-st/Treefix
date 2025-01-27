# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Registers a class with the Keras serialization framework."""
class_name = name if name is not None else arg.__name__
registered_name = package + '>' + class_name

if tf_inspect.isclass(arg) and not hasattr(arg, 'get_config'):
    raise ValueError(
        'Cannot register a class that does not have a get_config() method.')

if registered_name in _GLOBAL_CUSTOM_OBJECTS:
    raise ValueError(
        '%s has already been registered to %s' %
        (registered_name, _GLOBAL_CUSTOM_OBJECTS[registered_name]))

if arg in _GLOBAL_CUSTOM_NAMES:
    raise ValueError('%s has already been registered to %s' %
                     (arg, _GLOBAL_CUSTOM_NAMES[arg]))
_GLOBAL_CUSTOM_OBJECTS[registered_name] = arg
_GLOBAL_CUSTOM_NAMES[arg] = registered_name

exit(arg)
