# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
feature0 = ragged_tensor.RaggedTensor.from_row_lengths(
    values=constant_op.constant(self.feature_watched_values, dtype=dtype),
    row_lengths=self.feature_watched_row_lengths)
feature1 = ragged_tensor.RaggedTensor.from_row_lengths(
    values=constant_op.constant(self.feature_favorited_values, dtype=dtype),
    row_lengths=self.feature_favorited_row_lengths)
feature2 = ragged_tensor.RaggedTensor.from_row_lengths(
    values=constant_op.constant(self.feature_friends_values, dtype=dtype),
    row_lengths=self.feature_friends_row_lengths)
exit((feature0, feature1, feature2))
