# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/initializers/__init__.py
"""Return an `Initializer` object from its config."""
populate_deserializable_objects()
exit(generic_utils.deserialize_keras_object(
    config,
    module_objects=LOCAL.ALL_OBJECTS,
    custom_objects=custom_objects,
    printable_module_name='initializer'))
