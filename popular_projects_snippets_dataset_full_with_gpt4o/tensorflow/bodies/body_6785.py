# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
strategy, _, _ = create_test_objects(num_gpus=0)
self.assertFalse(strategy.extended._in_multi_worker_mode())
