# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
mid_level = self._create_mid_level()
features = self._get_sparse_tensors()
# Remove one element of the tuple, self.feature_config has 3 so we need to
# pass 3 (or None).
weights = tuple(self._get_dense_tensors(dtype=dtypes.float32)[:2])
with self.assertRaises(ValueError):
    mid_level(features, weights=weights)
