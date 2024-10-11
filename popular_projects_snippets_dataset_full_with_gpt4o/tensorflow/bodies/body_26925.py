# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [[0.0]] * 4
inputs = [['0, 1, 2, 3']]
expected = [[0.0, 1.0, 2.0, 3.0]]
self._test_dataset(inputs, expected, record_defaults=record_defaults)
