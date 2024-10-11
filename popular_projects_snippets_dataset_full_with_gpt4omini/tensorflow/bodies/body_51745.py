# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/serialization.py
"""Serializes a list of FeatureColumns.

  Returns a list of Keras-style config dicts that represent the input
  FeatureColumns and can be used with `deserialize_feature_columns` for
  reconstructing the original columns.

  Args:
    feature_columns: A list of FeatureColumns.

  Returns:
    Keras serialization for the list of FeatureColumns.

  Raises:
    ValueError if called with input that is not a list of FeatureColumns.
  """
exit([serialize_feature_column(fc) for fc in feature_columns])
