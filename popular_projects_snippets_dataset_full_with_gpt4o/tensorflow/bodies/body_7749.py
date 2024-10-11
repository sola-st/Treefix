# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
resolver = get_tpu_cluster_resolver()
remote.connect_to_cluster(resolver)
tpu_strategy_util.initialize_tpu_system(resolver)
strategy = tpu_lib.TPUStrategyV2(resolver)

config_proto = config_pb2.ConfigProto()
cluster_spec = server_lib.ClusterSpec({"worker": ["fake1", "fake2"]})
with test.mock.patch.object(
    resolver, "cluster_spec", return_value=cluster_spec):
    new_config = strategy.update_config_proto(config_proto)

# Verify cluster_def.
self.assertProtoEquals(cluster_spec.as_cluster_def(),
                       new_config.cluster_def)

# Verify isolate_session_state
self.assertTrue(new_config.isolate_session_state)
