# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Returns the class associated with `name` if it is registered with Keras.

  This function is part of the Keras serialization and deserialization
  framework. It maps strings to the objects associated with them for
  serialization/deserialization.

  Example:
  ```
  def from_config(cls, config, custom_objects=None):
    if 'my_custom_object_name' in config:
      config['hidden_cls'] = tf.keras.utils.get_registered_object(
          config['my_custom_object_name'], custom_objects=custom_objects)
  ```

  Args:
    name: The name to look up.
    custom_objects: A dictionary of custom objects to look the name up in.
      Generally, custom_objects is provided by the user.
    module_objects: A dictionary of custom objects to look the name up in.
      Generally, module_objects is provided by midlevel library implementers.

  Returns:
    An instantiable class associated with 'name', or None if no such class
      exists.
  """
if name in _GLOBAL_CUSTOM_OBJECTS:
    exit(_GLOBAL_CUSTOM_OBJECTS[name])
elif custom_objects and name in custom_objects:
    exit(custom_objects[name])
elif module_objects and name in module_objects:
    exit(module_objects[name])
exit(None)
