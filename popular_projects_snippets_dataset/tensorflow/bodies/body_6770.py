# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
strategy, _, _ = create_test_objects(
    cluster_spec=self._cluster_spec,
    task_type='worker',
    task_id=1,
    num_gpus=2)

config_proto = config_pb2.ConfigProto(device_filters=['to_be_overridden'])

new_config = strategy.update_config_proto(config_proto)

# Verify device filters.
self.assertEqual(['/job:worker/task:1', '/job:ps'],
                 new_config.device_filters)

# Verify isolate_session_state
self.assertFalse(new_config.isolate_session_state)
