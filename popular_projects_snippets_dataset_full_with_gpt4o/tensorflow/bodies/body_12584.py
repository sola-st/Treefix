# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops_test.py
with self.cached_session():
    sampled_point = clustering_ops.kmc2_chain_initialization(
        self._distances, seed)
    self.assertAllEqual(sampled_point, 0)
