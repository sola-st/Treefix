# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
strategy, _ = self._get_test_object(
    None, None, required_gpus, use_devices_arg=use_devices_arg)
self.assertEqual(required_gpus, strategy.num_replicas_in_sync)
