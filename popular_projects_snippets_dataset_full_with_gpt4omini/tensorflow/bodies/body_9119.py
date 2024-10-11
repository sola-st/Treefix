# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
# Adds a chief node, so there are NUM_WORKERS + 1 workers in total.
cluster_spec = copy.deepcopy(self._cluster_spec)
cluster_spec[CHIEF] = ["fake_chief"]

# Dumps the task contexts to the self._worker_context dict.
distribute_coordinator.run_distribute_coordinator(
    self._dump_worker_context,
    MockStrategy(between_graph=True),
    cluster_spec=cluster_spec,
    rpc_layer="grpc")

# There are one CHIEF and three workers.
self.assertEqual(len(self._worker_context), 2)
self.assertTrue(CHIEF in self._worker_context)
self.assertTrue(WORKER in self._worker_context)
self.assertEqual(len(self._worker_context[CHIEF]), 1)
self.assertEqual(len(self._worker_context[WORKER]), NUM_WORKERS)

# Check whether each task has the right master_target, num_workers, is_chief
# and distributed_mode.
self.assertEqual(self._worker_context[CHIEF][0],
                 ("grpc://fake_chief", 4, True, True))
self.assertEqual(
    self._worker_context[WORKER][0],
    (_bytes_to_str(self._workers[0].target), NUM_WORKERS + 1, False, True))
self.assertEqual(
    self._worker_context[WORKER][1],
    (_bytes_to_str(self._workers[1].target), NUM_WORKERS + 1, False, True))
self.assertEqual(
    self._worker_context[WORKER][2],
    (_bytes_to_str(self._workers[2].target), NUM_WORKERS + 1, False, True))
