# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops_test.py
with self.cached_session():
    [indices, distances] = clustering_ops.nearest_neighbors(self._points,
                                                            self._centers, 2)
    self.assertAllClose(indices, [[0, 1], [0, 1], [1, 0], [4, 3]])
    self.assertAllClose(distances, [[0., 2.], [5., 5.], [1., 5.], [0., 2.]])
