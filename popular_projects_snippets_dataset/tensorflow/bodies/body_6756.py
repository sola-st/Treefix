# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
strategy, _, _ = create_test_objects(num_gpus=0)
self._test_device_assignment_local(
    strategy, compute_device='CPU', variable_device='CPU', num_gpus=0)
