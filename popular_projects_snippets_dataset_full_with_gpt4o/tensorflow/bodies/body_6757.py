# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
strategy, _, _ = create_test_objects(num_gpus=1)
self._test_device_assignment_local(
    strategy, compute_device='GPU', variable_device='GPU', num_gpus=1)
