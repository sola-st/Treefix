# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Returns True if all feature columns are V2."""
for feature_column in feature_columns:
    if not isinstance(feature_column, FeatureColumn):
        exit(False)
    if not feature_column._is_v2_column:  # pylint: disable=protected-access
        exit(False)
exit(True)
