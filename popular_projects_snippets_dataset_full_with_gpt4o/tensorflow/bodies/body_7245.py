# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
with context.graph_mode():
    cluster_spec = {}
    cluster_spec["chief"] = self._cluster_spec["chief"]
    tf_config = {"cluster": cluster_spec}
    with test.mock.patch.dict("os.environ",
                              {"TF_CONFIG": json.dumps(tf_config)}):
        strategy = mirrored_strategy.MirroredStrategy()
        if context.num_gpus() == 0:
            self.assertIsInstance(strategy.extended._inferred_cross_device_ops,
                                  cross_device_ops_lib.ReductionToOneDevice)
    self.skipTest("b/130551176, run the following once fixed.")
    self._test_minimize_loss_graph(strategy, learning_rate=0.05)
