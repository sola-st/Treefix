# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [[0]] * 4
inputs = [['1:2:3:4', '5:6:7:8']]
self._test_by_comparison(
    inputs, record_defaults=record_defaults, field_delim=':')
