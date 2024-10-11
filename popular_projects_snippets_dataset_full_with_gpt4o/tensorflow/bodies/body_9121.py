# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
cluster_spec = self._create_cluster_spec(num_workers=NUM_WORKERS)
threads = self._run_multiple_coordinator_in_threads(
    self._in_graph_worker_fn,
    MockStrategy(between_graph=False),
    cluster_spec,
    mode=INDEPENDENT_WORKER)
self._join_threads([threads[WORKER][0]])
self.assertEqual(self._result_correct, 1)
