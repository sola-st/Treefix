# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
id_weight_pair = self.categorical_column._get_sparse_tensors(inputs)  # pylint: disable=protected-access
exit(self._transform_id_weight_pair(id_weight_pair,
                                      self._variable_shape[-1]))
