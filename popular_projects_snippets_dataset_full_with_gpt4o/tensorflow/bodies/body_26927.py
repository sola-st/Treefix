# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [[0.0]] * 2
inputs = [['0,1,2,3']]
self._test_dataset(
    inputs,
    expected_err_re='Expect 2 fields but have more in record',
    record_defaults=record_defaults)
