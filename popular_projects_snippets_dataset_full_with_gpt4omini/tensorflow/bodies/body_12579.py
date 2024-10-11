# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops_test.py
with self.cached_session():
    distances = np.zeros(1000).astype(np.float32)
    distances[6] = 10e7
    distances[4] = 10e3

    sampled_point = clustering_ops.kmc2_chain_initialization(distances, seed)
    self.assertAllEqual(sampled_point, 6)
    distances[6] = 0.0
    sampled_point = clustering_ops.kmc2_chain_initialization(distances, seed)
    self.assertAllEqual(sampled_point, 4)
