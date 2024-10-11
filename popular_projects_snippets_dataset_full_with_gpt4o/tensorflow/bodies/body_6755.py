# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
strategy, _, _ = create_test_objects(num_gpus=2)
# All the devices on a given worker are in sync which in this case is the
# number of gpus on each worker.
self.assertEqual(2, strategy.num_replicas_in_sync)
