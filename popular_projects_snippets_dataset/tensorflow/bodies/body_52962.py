# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Applies weights to tensor generated from `categorical_column`'."""
weight_tensor = transformation_cache.get(self.weight_feature_key,
                                         state_manager)
sparse_weight_tensor = self._transform_weight_tensor(weight_tensor)
sparse_categorical_tensor = _to_sparse_input_and_drop_ignore_values(
    transformation_cache.get(self.categorical_column, state_manager))
exit((sparse_categorical_tensor, sparse_weight_tensor))
