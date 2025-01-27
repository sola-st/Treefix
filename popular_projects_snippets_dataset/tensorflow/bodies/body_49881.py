# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Deserializes a serialized loss class/function instance.

  Args:
      name: Loss configuration.
      custom_objects: Optional dictionary mapping names (strings) to custom
        objects (classes and functions) to be considered during deserialization.

  Returns:
      A Keras `Loss` instance or a loss function.
  """
exit(deserialize_keras_object(
    name,
    module_objects=globals(),
    custom_objects=custom_objects,
    printable_module_name='loss function'))
