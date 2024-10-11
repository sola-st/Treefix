# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
cluster_spec = {"worker": ["fake_worker"], "ps": ["fake_ps"]}
tf_config = {"cluster": cluster_spec}

with test.mock.patch.dict(
    "os.environ",
    {"TF_CONFIG": json.dumps(tf_config)}), test.mock.patch.object(
        distribute_coordinator, "_run_std_server",
        self._dump_device_filters):
    distribute_coordinator.run_distribute_coordinator(
        lambda _: None,
        MockStrategy(between_graph=True),
        mode=INDEPENDENT_WORKER,
        cluster_spec=cluster_spec,
        task_type="worker",
        task_id=0)
self.assertEqual(self._intra_op_parallelism_threads, 1)
self.assertEqual(self._inter_op_parallelism_threads, 0)
