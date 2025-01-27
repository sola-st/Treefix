# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops_test.py
with self.cached_session():
    [indices, distances] = clustering_ops.nearest_neighbors(self._points,
                                                            self._centers, 1)
    self.assertAllClose(indices, [[0], [0], [1], [4]])
    self.assertAllClose(distances, [[0.], [5.], [1.], [0.]])
