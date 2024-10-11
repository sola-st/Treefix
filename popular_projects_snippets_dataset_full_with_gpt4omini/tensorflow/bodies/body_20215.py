# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
feature0 = sparse_tensor.SparseTensor(
    indices=self.feature_watched_indices,
    values=constant_op.constant(self.feature_watched_values, dtype=dtype),
    dense_shape=[self.data_batch_size, 2])
feature1 = sparse_tensor.SparseTensor(
    indices=self.feature_favorited_indices,
    values=constant_op.constant(self.feature_favorited_values, dtype=dtype),
    dense_shape=[self.data_batch_size, 2])
feature2 = sparse_tensor.SparseTensor(
    indices=self.feature_friends_indices,
    values=constant_op.constant(self.feature_friends_values, dtype=dtype),
    dense_shape=[self.data_batch_size, 3])
exit((feature0, feature1, feature2))
