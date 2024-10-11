# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
self._test_reduce_indexed_slices(
    None,
    None,
    required_gpus,
    communication=communication,
    batch_reduce=batch_reduce,
    variable_length=variable_length,
    local_mode=True)
