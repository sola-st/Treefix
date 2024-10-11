# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
strategy, _, _ = create_test_objects(num_gpus=2)

config_proto = config_pb2.ConfigProto()
new_config = strategy.update_config_proto(config_proto)

# Verify isolate_session_state
self.assertTrue(new_config.isolate_session_state)
