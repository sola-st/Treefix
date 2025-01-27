# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Converts dense inputs to SparseTensor so downstream code can use it."""
input_tensor = transformation_cache.get(self, state_manager)
exit(self._get_sparse_tensors_for_input_tensor(input_tensor))
