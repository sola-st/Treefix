# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
# Dumps the task contexts to the self._worker_context dict.
distribute_coordinator.run_distribute_coordinator(
    self._dump_worker_context,
    MockStrategy(between_graph=True),
    cluster_spec=self._cluster_spec)

# There is only one type of task and there three such tasks.
self.assertEqual(len(self._worker_context), 1)
self.assertTrue(WORKER in self._worker_context)
self.assertEqual(len(self._worker_context[WORKER]), NUM_WORKERS)

# Check whether each task has the right master_target, num_workers, is_chief
# and distributed_mode.
self.assertEqual(
    self._worker_context[WORKER][0],
    (_bytes_to_str(self._workers[0].target), NUM_WORKERS, True, True))
self.assertEqual(
    self._worker_context[WORKER][1],
    (_bytes_to_str(self._workers[1].target), NUM_WORKERS, False, True))
self.assertEqual(
    self._worker_context[WORKER][2],
    (_bytes_to_str(self._workers[2].target), NUM_WORKERS, False, True))
