# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_initialization_test.py
# Dequeue on CPU.
mid_level_api = self._create_mid_level()
with self.assertRaises(RuntimeError):
    mid_level_api.dequeue()
# Enqueue on CPU.
features = {
    'watched': sparse_tensor.SparseTensor(
        indices=self.feature_watched_indices,
        values=self.feature_watched_values,
        dense_shape=[2, 2])}
with self.assertRaises(RuntimeError):
    mid_level_api.enqueue(features)
# Apply gradient on CPU.
mid_level_api = self._create_mid_level()
with self.assertRaises(RuntimeError):
    mid_level_api.apply_gradients(None)
