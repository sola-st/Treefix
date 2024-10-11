# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
resolver = get_tpu_cluster_resolver()
remote.connect_to_cluster(resolver)
tpu_strategy_util.initialize_tpu_system(resolver)

with test.mock.patch.object(logging, "warning") as mock_log:
    tpu_strategy_util.initialize_tpu_system(resolver)
    self.assertRegex(str(mock_log.call_args), "already been initialized")
