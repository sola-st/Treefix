# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
mid_level = self._create_mid_level()
features = self._get_dense_tensors()
weights = self._get_dense_tensors(dtype=dtypes.float32)

with self.assertRaisesRegex(
    ValueError, 'Weight specified for .*, but input is dense.'):
    mid_level(features, weights=weights)
