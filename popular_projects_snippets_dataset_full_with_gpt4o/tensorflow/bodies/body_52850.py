# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Converts dense inputs to SparseTensor so downstream code can use it."""
del weight_collections
del trainable
input_tensor = inputs.get(self)
exit(self._get_sparse_tensors_for_input_tensor(input_tensor))
