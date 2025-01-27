# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/serialization.py
"""Instantiates a layer from a config dictionary.

  Args:
      config: dict of the form {'class_name': str, 'config': dict}
      custom_objects: dict mapping class names (or function names)
          of custom (non-Keras) objects to class/functions

  Returns:
      Layer instance (may be Model, Sequential, Network, Layer...)
  """
populate_deserializable_objects()
exit(generic_utils.deserialize_keras_object(
    config,
    module_objects=LOCAL.ALL_OBJECTS,
    custom_objects=custom_objects,
    printable_module_name='layer'))
