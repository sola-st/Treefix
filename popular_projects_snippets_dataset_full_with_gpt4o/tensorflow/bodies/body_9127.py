# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
# Adds a EVALUATOR job.
cluster_spec = self._create_cluster_spec(
    num_workers=NUM_WORKERS, has_eval=True)

# Dumps the task contexts and std server arguments.
with test.mock.patch.object(distribute_coordinator, "_run_std_server",
                            self._run_mock_std_server):
    threads = self._run_multiple_coordinator_in_threads(
        self._dump_worker_context,
        MockStrategy(between_graph=False),
        cluster_spec,
        mode=INDEPENDENT_WORKER,
        rpc_layer=None)
    self._join_threads(threads[WORKER])
    self._join_threads([threads[EVALUATOR][0]])

# There are one "None" task and one EVALUATOR task.
self.assertEqual(len(self._worker_context), 2)
self.assertTrue("None" in self._worker_context)
self.assertTrue(EVALUATOR in self._worker_context)
self.assertEqual(len(self._worker_context["None"]), 1)
self.assertEqual(len(self._worker_context[EVALUATOR]), 1)

# Check whether each task has the right master_target, num_workers, is_chief
# and distributed_mode.
self.assertEqual(self._worker_context["None"][0],
                 (_bytes_to_str(cluster_spec[WORKER][0]), 3, True, True))
self.assertEqual(self._worker_context[EVALUATOR][0], ("", 3, True, False))

# Make sure each worker runs a std server.
self.assertEqual(len(self._std_servers), 1)
self.assertTrue(WORKER in self._std_servers)
self.assertEqual(len(self._std_servers[WORKER]), 3)
self.assertFalse(self._std_servers[WORKER][0].joined)
self.assertTrue(self._std_servers[WORKER][1].joined)
self.assertTrue(self._std_servers[WORKER][2].joined)
