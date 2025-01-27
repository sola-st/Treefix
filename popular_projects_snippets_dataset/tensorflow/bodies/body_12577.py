# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops_test.py
with self.cached_session():
    sampled_points = clustering_ops.kmeans_plus_plus_initialization(
        self._points, 3, seed, (seed % 5) - 1)
    self.assertAllClose(
        sorted(self.evaluate(sampled_points).tolist()),
        [[-1., -1.], [101., 1.], [101., 1.]],
        atol=1.0)
