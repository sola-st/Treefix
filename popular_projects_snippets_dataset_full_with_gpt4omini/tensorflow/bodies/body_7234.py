# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
distribution.configure(cluster_spec={"worker": ["fake1", "fake2"]})

config_proto = config_pb2.ConfigProto()
new_config = distribution.update_config_proto(config_proto)

# Verify isolate_session_state
self.assertTrue(new_config.isolate_session_state)
