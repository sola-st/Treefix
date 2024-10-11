# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
mid_level = self._create_mid_level()
# Remove one element of the tuple, self.feature_config has 3 so we need to
# pass 3.
features = tuple(self._get_sparse_tensors()[:2])
with self.assertRaises(ValueError):
    mid_level(features, weights=None)
