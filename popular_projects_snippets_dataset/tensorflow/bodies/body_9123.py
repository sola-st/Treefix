# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
cluster_spec = self._create_cluster_spec(
    num_workers=NUM_WORKERS, num_ps=NUM_PS)
threads = self._run_multiple_coordinator_in_threads(
    self._between_graph_with_monitored_session,
    MockStrategy(between_graph=True),
    cluster_spec,
    mode=INDEPENDENT_WORKER)
self._join_threads(threads[WORKER])

# Each finished worker will increment self._result_correct.
self.assertEqual(self._result_correct, NUM_WORKERS)
