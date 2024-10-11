# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [['NA']]
inputs = [['0', '', '2']]
self._test_dataset(
    inputs, [['0'], ['NA'], ['2']], record_defaults=record_defaults)
