# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops_test.py
with self.cached_session():
    [indices, distances] = clustering_ops.nearest_neighbors(self._points,
                                                            self._centers, 5)
    self.assertAllClose(
        indices,
        self._expected_nearest_neighbor_indices[:, 0:5])
    self.assertAllClose(
        distances,
        self._expected_nearest_neighbor_squared_distances[:, 0:5])
