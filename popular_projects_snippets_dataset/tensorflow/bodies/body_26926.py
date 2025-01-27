# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [[]] * 2
inputs = [['0,']]
self._test_dataset(
    inputs,
    expected_err_re='Field 1 is required but missing in record!',
    record_defaults=record_defaults)
