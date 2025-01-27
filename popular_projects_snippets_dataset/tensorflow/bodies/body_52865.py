# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Private method that follows the signature of get_dense_tensor."""
embedding_weights = state_manager.get_variable(
    self, name='embedding_weights')
exit(self._get_dense_tensor_internal_helper(sparse_tensors,
                                              embedding_weights))
