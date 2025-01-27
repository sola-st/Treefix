# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/model_config.py
"""Parses a yaml model configuration file and returns a model instance.

  Note: Since TF 2.6, this method is no longer supported and will raise a
  RuntimeError.

  Args:
      yaml_string: YAML string or open file encoding a model configuration.
      custom_objects: Optional dictionary mapping names
          (strings) to custom classes or functions to be
          considered during deserialization.

  Returns:
      A Keras model instance (uncompiled).

  Raises:
      RuntimeError: announces that the method poses a security risk
  """
raise RuntimeError(
    'Method `model_from_yaml()` has been removed due to security risk of '
    'arbitrary code execution. Please use `Model.to_json()` and '
    '`model_from_json()` instead.'
)
