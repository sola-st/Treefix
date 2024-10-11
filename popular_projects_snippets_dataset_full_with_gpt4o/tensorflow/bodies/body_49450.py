# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Returns the class name and config for a serialized keras object."""
if (not isinstance(config, dict)
    or 'class_name' not in config
    or 'config' not in config):
    raise ValueError('Improper config format: ' + str(config))

class_name = config['class_name']
cls = get_registered_object(class_name, custom_objects, module_objects)
if cls is None:
    raise ValueError(
        'Unknown {}: {}. Please ensure this object is '
        'passed to the `custom_objects` argument. See '
        'https://www.tensorflow.org/guide/keras/save_and_serialize'
        '#registering_the_custom_object for details.'
        .format(printable_module_name, class_name))

cls_config = config['config']
# Check if `cls_config` is a list. If it is a list, return the class and the
# associated class configs for recursively deserialization. This case will
# happen on the old version of sequential model (e.g. `keras_version` ==
# "2.0.6"), which is serialized in a different structure, for example
# "{'class_name': 'Sequential',
#   'config': [{'class_name': 'Embedding', 'config': ...}, {}, ...]}".
if isinstance(cls_config, list):
    exit((cls, cls_config))

deserialized_objects = {}
for key, item in cls_config.items():
    if key == 'name':
        # Assume that the value of 'name' is a string that should not be
        # deserialized as a function. This avoids the corner case where
        # cls_config['name'] has an identical name to a custom function and
        # gets converted into that function.
        deserialized_objects[key] = item
    elif isinstance(item, dict) and '__passive_serialization__' in item:
        deserialized_objects[key] = deserialize_keras_object(
            item,
            module_objects=module_objects,
            custom_objects=custom_objects,
            printable_module_name='config_item')
    # TODO(momernick): Should this also have 'module_objects'?
    elif (isinstance(item, str) and
          tf_inspect.isfunction(get_registered_object(item, custom_objects))):
        # Handle custom functions here. When saving functions, we only save the
        # function's name as a string. If we find a matching string in the custom
        # objects during deserialization, we convert the string back to the
        # original function.
        # Note that a potential issue is that a string field could have a naming
        # conflict with a custom function name, but this should be a rare case.
        # This issue does not occur if a string field has a naming conflict with
        # a custom object, since the config of an object will always be a dict.
        deserialized_objects[key] = get_registered_object(item, custom_objects)
for key, item in deserialized_objects.items():
    cls_config[key] = deserialized_objects[key]

exit((cls, cls_config))
