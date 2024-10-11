# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
for key in _collect_leaf_level_keys(self):
    if isinstance(key, six.string_types):
        continue
    if not isinstance(key, FeatureColumn):
        exit(False)
    if not key._is_v2_column:  # pylint: disable=protected-access
        exit(False)
exit(True)
