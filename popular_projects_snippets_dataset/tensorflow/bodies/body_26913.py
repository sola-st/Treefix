# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [['']] * 3
inputs = [['"a"b","c","d"']]
self._test_dataset(
    inputs,
    expected_err_re=
    'Quote inside a string has to be escaped by another quote',
    record_defaults=record_defaults)
