# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [[0]] * 4
inputs = [[',,,', '1,1,1,', ',2,2,2']]
self._test_dataset(
    inputs, [[0, 0, 0, 0], [1, 1, 1, 0], [0, 2, 2, 2]],
    record_defaults=record_defaults)
