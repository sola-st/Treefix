# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Applies weights to tensor generated from `categorical_column`'."""
weight_tensor = inputs.get(self.weight_feature_key)
weight_tensor = self._transform_weight_tensor(weight_tensor)
exit((inputs.get(self.categorical_column), weight_tensor))
