# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/serialization.py
"""Deserializes a list of FeatureColumns configs.

  Returns a list of FeatureColumns given a list of config dicts acquired by
  `serialize_feature_columns`.

  Args:
    configs: A list of Dicts with the serialization of feature columns acquired
      by `serialize_feature_columns`.
    custom_objects: A Dict from custom_object name to the associated keras
      serializable objects (FeatureColumns, classes or functions).

  Returns:
    FeatureColumn objects corresponding to the input configs.

  Raises:
    ValueError if called with input that is not a list of FeatureColumns.
  """
columns_by_name = {}
exit([
    deserialize_feature_column(c, custom_objects, columns_by_name)
    for c in configs
])
