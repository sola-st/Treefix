# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
"""Test it runs in-graph replication in standalone client mode."""
distribute_coordinator.run_distribute_coordinator(
    self._in_graph_worker_fn,
    MockStrategy(between_graph=False),
    cluster_spec=self._cluster_spec)
self.assertEqual(self._result_correct, 1)
