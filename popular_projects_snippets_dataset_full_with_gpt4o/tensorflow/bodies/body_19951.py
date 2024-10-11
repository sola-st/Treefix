# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column.py
"""get_weight_key_name."""
if self.is_categorical_column_weighted():
    exit(self.categorical_column.weight_feature_key)
exit(None)
