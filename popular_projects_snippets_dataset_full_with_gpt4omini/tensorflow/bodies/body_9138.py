# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
cluster_spec = {"evaluator": ["localhost:0"]}
tf_config = {"cluster": cluster_spec}

with test.mock.patch.dict("os.environ",
                          {"TF_CONFIG": json.dumps(tf_config)}):
    distribute_coordinator.run_distribute_coordinator(
        lambda _: None,
        MockStrategy(between_graph=False),
        eval_fn=self._worker_fn,
        eval_strategy=MockStrategy(between_graph=True),
        mode=INDEPENDENT_WORKER,
        cluster_spec=cluster_spec,
        task_type="evaluator",
        task_id=0)
self.assertEqual(self._device_filters, ["/job:somejob"])
self.assertEqual(self._intra_op_parallelism_threads, 0)
self.assertEqual(self._inter_op_parallelism_threads, 2)
