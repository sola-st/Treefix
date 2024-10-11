# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
cluster_spec = {"worker": ["localhost:0"]}
tf_config = {"cluster": cluster_spec}

# Reset the saved Server state.
distribute_coordinator._thread_local = threading.local()  # pylint: disable=protected-access

with test.mock.patch.dict("os.environ",
                          {"TF_CONFIG": json.dumps(tf_config)}):
    distribute_coordinator.run_distribute_coordinator(
        self._worker_fn,
        MockStrategy(between_graph=True),
        mode=INDEPENDENT_WORKER,
        cluster_spec=cluster_spec,
        task_type="worker",
        task_id=0)
self.assertEqual(self._device_filters, ["/job:worker/task:0", "/job:ps"])
self.assertEqual(self._intra_op_parallelism_threads, 2)
self.assertEqual(self._inter_op_parallelism_threads, 0)
