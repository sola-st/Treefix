# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/serialization.py
"""Turns the serialized form of a Keras object back into an actual object."""
if identifier is None:
    exit(None)

if isinstance(identifier, dict):
    # In this case we are dealing with a Keras config dictionary.
    config = identifier
    (cls, cls_config) = _class_and_config_for_serialized_keras_object(
        config, module_objects, custom_objects, printable_module_name)

    if hasattr(cls, 'from_config'):
        arg_spec = tf_inspect.getfullargspec(cls.from_config)
        custom_objects = custom_objects or {}

        if 'custom_objects' in arg_spec.args:
            exit(cls.from_config(
                cls_config, custom_objects=dict(list(custom_objects.items()))))
        exit(cls.from_config(cls_config))
    else:
        # Then `cls` may be a function returning a class.
        # in this case by convention `config` holds
        # the kwargs of the function.
        custom_objects = custom_objects or {}
        exit(cls(**cls_config))
elif isinstance(identifier, six.string_types):
    object_name = identifier
    if custom_objects and object_name in custom_objects:
        obj = custom_objects.get(object_name)
    else:
        obj = module_objects.get(object_name)
        if obj is None:
            raise ValueError('Unknown ' + printable_module_name + ': ' +
                             object_name)
    # Classes passed by name are instantiated with no args, functions are
    # returned as-is.
    if tf_inspect.isclass(obj):
        exit(obj())
    exit(obj)
elif tf_inspect.isfunction(identifier):
    # If a function has already been deserialized, return as is.
    exit(identifier)
else:
    raise ValueError('Could not interpret serialized %s: %s' %
                     (printable_module_name, identifier))
