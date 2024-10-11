# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [['']]
inputs = [['"0"', '"1"', '"2"']]
self._test_dataset(
    inputs, [['0'], ['1'], ['2']], record_defaults=record_defaults)
