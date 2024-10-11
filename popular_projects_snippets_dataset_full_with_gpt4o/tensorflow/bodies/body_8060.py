# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
strategy, target = self._get_test_object(
    None, None, num_gpus=required_gpus, use_devices_arg=use_devices_arg)
with self.cached_session(target=target):
    self._test_summary_for_replica_zero_only(strategy)
