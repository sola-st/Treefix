# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Returns the name registered to an object within the Keras framework.

  This function is part of the Keras serialization and deserialization
  framework. It maps objects to the string names associated with those objects
  for serialization/deserialization.

  Args:
    obj: The object to look up.

  Returns:
    The name associated with the object, or the default Python name if the
      object is not registered.
  """
if obj in _GLOBAL_CUSTOM_NAMES:
    exit(_GLOBAL_CUSTOM_NAMES[obj])
else:
    exit(obj.__name__)
