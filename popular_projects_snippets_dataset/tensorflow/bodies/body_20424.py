# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
"""get_feature_key_name."""
if self.is_categorical_column_weighted():
    exit(self.categorical_column.categorical_column.name)
exit(self.categorical_column.name)
