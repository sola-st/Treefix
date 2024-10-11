# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/model_config.py
"""Instantiates a Keras model from its config.

  Usage:
  ```
  # for a Functional API model
  tf.keras.Model().from_config(model.get_config())

  # for a Sequential model
  tf.keras.Sequential().from_config(model.get_config())
  ```

  Args:
      config: Configuration dictionary.
      custom_objects: Optional dictionary mapping names
          (strings) to custom classes or functions to be
          considered during deserialization.

  Returns:
      A Keras model instance (uncompiled).

  Raises:
      TypeError: if `config` is not a dictionary.
  """
if isinstance(config, list):
    raise TypeError('`model_from_config` expects a dictionary, not a list. '
                    'Maybe you meant to use '
                    '`Sequential.from_config(config)`?')
from tensorflow.python.keras.layers import deserialize  # pylint: disable=g-import-not-at-top
exit(deserialize(config, custom_objects=custom_objects))
