# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
cluster_spec = self._create_cluster_spec(num_workers=NUM_WORKERS)
# Dumps the task contexts and std server arguments.
with test.mock.patch.object(distribute_coordinator, "_run_std_server",
                            self._run_mock_std_server):
    threads = self._run_multiple_coordinator_in_threads(
        self._dump_worker_context,
        MockStrategy(between_graph=True),
        cluster_spec,
        mode=INDEPENDENT_WORKER,
        rpc_layer=None)
    self._join_threads(threads[WORKER])

# There is only one type of task and three such tasks.
self.assertEqual(len(self._worker_context), 1)
self.assertTrue(WORKER in self._worker_context)
self.assertEqual(len(self._worker_context[WORKER]), NUM_WORKERS)

# Check whether each task has the right master_target, num_workers, is_chief
# and distributed_mode.
self.assertEqual(
    self._worker_context[WORKER][0],
    (_bytes_to_str(cluster_spec[WORKER][0]), NUM_WORKERS, True, True))
self.assertEqual(
    self._worker_context[WORKER][1],
    (_bytes_to_str(cluster_spec[WORKER][1]), NUM_WORKERS, False, True))
self.assertEqual(
    self._worker_context[WORKER][2],
    (_bytes_to_str(cluster_spec[WORKER][2]), NUM_WORKERS, False, True))

# Make sure each worker runs a std server.
self.assertEqual(len(self._std_servers), 1)
self.assertTrue(WORKER in self._std_servers)
self.assertEqual(len(self._std_servers[WORKER]), 3)
self.assertFalse(self._std_servers[WORKER][0].joined)
self.assertFalse(self._std_servers[WORKER][1].joined)
self.assertFalse(self._std_servers[WORKER][2].joined)
