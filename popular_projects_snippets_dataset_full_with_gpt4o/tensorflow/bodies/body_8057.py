# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
strategy, target = self._get_test_object(
    None, None, num_gpus=required_gpus, use_devices_arg=use_devices_arg)
self._test_numpy_dataset(
    strategy, session=self.cached_session(target=target))
