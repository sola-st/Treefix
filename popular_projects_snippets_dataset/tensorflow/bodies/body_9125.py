# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
cluster_spec = self._create_cluster_spec(num_workers=NUM_WORKERS)
# Dumps properties of the strategy objects.
with test.mock.patch.object(distribute_coordinator, "_run_std_server",
                            self._run_mock_std_server):
    threads = self._run_multiple_coordinator_in_threads(
        self._dump_strategy_property,
        MockStrategy(between_graph=True, should_init=True),
        cluster_spec,
        mode=INDEPENDENT_WORKER,
        rpc_layer=None)
    self._join_threads(threads[WORKER])

# There is only one type of task and there three such tasks.
self.assertEqual(len(self._strategy_property), 1)
self.assertTrue(WORKER in self._strategy_property)
self.assertEqual(len(self._strategy_property[WORKER]), NUM_WORKERS)

# Check whether each task has the right properties of should_init,
# should_checkpoint and should_save_summary.
self.assertEqual(self._strategy_property[WORKER][0], (True, True, True))
self.assertEqual(self._strategy_property[WORKER][1], (True, False, False))
self.assertEqual(self._strategy_property[WORKER][2], (True, False, False))
