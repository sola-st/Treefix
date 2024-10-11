# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
"""Test monitored session in standalone client mode."""
distribute_coordinator.run_distribute_coordinator(
    self._between_graph_with_monitored_session,
    MockStrategy(between_graph=True),
    cluster_spec=self._cluster_spec)

# Each finished worker will increment self._result_correct.
self.assertEqual(self._result_correct, NUM_WORKERS)
