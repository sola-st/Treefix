# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
mid_level = self._create_mid_level()
features = self._get_sparse_tensors()
weights = self._get_dense_tensors(dtype=dtypes.float32)
with self.assertRaisesRegex(
    ValueError, 'but it does not match type of the input which is'):
    mid_level(features, weights=weights)
