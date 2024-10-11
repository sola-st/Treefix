# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
with context.graph_mode():
    tf_config = {"cluster": self._cluster_spec}
    with test.mock.patch.dict("os.environ",
                              {"TF_CONFIG": json.dumps(tf_config)}):
        strategy = mirrored_strategy.MirroredStrategy(
            cross_device_ops=self._make_cross_device_ops())
        self.assertEqual(
            max(context.num_gpus(), 1) * 3, strategy.num_replicas_in_sync)
