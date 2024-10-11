# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
distribution, target = self._get_test_object(
    None, None, num_gpus=required_gpus, use_devices_arg=use_devices_arg)
with self.cached_session(target=target):
    self._test_all_reduce_sum_gradient_tape(distribution)
