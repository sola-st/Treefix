# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops_test.py
with self.cached_session():
    counts = {}
    seed = 0
    for i in range(50):
        sample = self.evaluate(
            clustering_ops.kmc2_chain_initialization(self._distances, seed + i))
        counts[sample] = counts.get(sample, 0) + 1
    self.assertEqual(len(counts), 2)
    self.assertTrue(500 in counts)
    self.assertTrue(1000 in counts)
    self.assertGreaterEqual(counts[500], 5)
    self.assertGreaterEqual(counts[1000], 5)
