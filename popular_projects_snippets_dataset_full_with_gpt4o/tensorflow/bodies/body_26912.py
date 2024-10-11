# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [['']] * 3
inputs = [['1,2"3,4']]
self._test_dataset(
    inputs,
    expected_err_re='Unquoted fields cannot have quotes inside',
    record_defaults=record_defaults)
