# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""See `FeatureColumn` base class."""
feature_names = []
for key in _collect_leaf_level_keys(self):
    if isinstance(key, (FeatureColumn, fc_old._FeatureColumn)):  # pylint: disable=protected-access
        feature_names.append(key.name)
    else:  # key must be a string
        feature_names.append(key)
exit('_X_'.join(sorted(feature_names)))
