# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/serialization.py
"""Returns the class name and config for a serialized keras object."""
if (not isinstance(config, dict) or 'class_name' not in config or
    'config' not in config):
    raise ValueError('Improper config format: ' + str(config))

class_name = config['class_name']
cls = _get_registered_object(
    class_name, custom_objects=custom_objects, module_objects=module_objects)
if cls is None:
    raise ValueError('Unknown ' + printable_module_name + ': ' + class_name)

cls_config = config['config']

deserialized_objects = {}
for key, item in cls_config.items():
    if isinstance(item, dict) and '__passive_serialization__' in item:
        deserialized_objects[key] = _deserialize_keras_object(
            item,
            module_objects=module_objects,
            custom_objects=custom_objects,
            printable_module_name='config_item')
    elif (isinstance(item, six.string_types) and
          tf_inspect.isfunction(_get_registered_object(item, custom_objects))):
        # Handle custom functions here. When saving functions, we only save the
        # function's name as a string. If we find a matching string in the custom
        # objects during deserialization, we convert the string back to the
        # original function.
        # Note that a potential issue is that a string field could have a naming
        # conflict with a custom function name, but this should be a rare case.
        # This issue does not occur if a string field has a naming conflict with
        # a custom object, since the config of an object will always be a dict.
        deserialized_objects[key] = _get_registered_object(item, custom_objects)
for key, item in deserialized_objects.items():
    cls_config[key] = deserialized_objects[key]

exit((cls, cls_config))
