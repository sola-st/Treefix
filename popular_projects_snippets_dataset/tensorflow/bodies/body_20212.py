# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
feature0 = constant_op.constant(self.feature_watched_values, dtype=dtype)
feature1 = constant_op.constant(self.feature_favorited_values, dtype=dtype)
feature2 = constant_op.constant(self.feature_friends_values, dtype=dtype)
exit((feature0, feature1, feature2))
