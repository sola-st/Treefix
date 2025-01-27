# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
self._test_reduction(
    None,
    None,
    required_gpus,
    communication=communication,
    use_strategy_object=use_strategy_object,
    local_mode=True)
