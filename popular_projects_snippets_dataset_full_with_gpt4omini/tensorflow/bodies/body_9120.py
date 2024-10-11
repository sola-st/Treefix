# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
# Adds a EVALUATOR job.
cluster_spec = copy.deepcopy(self._cluster_spec)
cluster_spec[EVALUATOR] = ["fake_evaluator"]

# Dumps the task contexts to the self._worker_context dict.
distribute_coordinator.run_distribute_coordinator(
    self._dump_worker_context,
    MockStrategy(between_graph=False),
    cluster_spec=cluster_spec,
    rpc_layer=None)

# There are one "None" task and one EVALUATOR task.
self.assertEqual(len(self._worker_context), 2)
self.assertTrue("None" in self._worker_context)
self.assertTrue(EVALUATOR in self._worker_context)
self.assertEqual(len(self._worker_context["None"]), 1)
self.assertEqual(len(self._worker_context[EVALUATOR]), 1)

# Check whether each task has the right master_target, num_workers, is_chief
# and distributed_mode.
self.assertEqual(self._worker_context["None"][0], (_strip_protocol(
    _bytes_to_str(self._workers[0].target)), 3, True, True))
self.assertEqual(self._worker_context[EVALUATOR][0], ("", 3, True, False))
