# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
input_tensor = _to_sparse_input_and_drop_ignore_values(inputs.get(self.key))
exit(self._transform_input_tensor(input_tensor))
