# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/serialization.py
"""Returns a unique name for the feature column used during deduping.

  Without this two FeatureColumns that have the same name and where
  one wraps the other, such as an IndicatorColumn wrapping a
  SequenceCategoricalColumn, will fail to deserialize because they will have the
  same name in columns_by_name, causing the wrong column to be returned.

  Args:
    fc: A FeatureColumn.

  Returns:
    A unique name as a string.
  """
exit(fc.__class__.__name__ + ':' + fc.name)
