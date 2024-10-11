# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [['']] * 2
inputs = [['']]  # Empty file
self._test_dataset(
    inputs, expected_output=[], record_defaults=record_defaults)
