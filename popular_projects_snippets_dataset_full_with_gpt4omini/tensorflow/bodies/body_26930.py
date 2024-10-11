# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [[0]] * 2
inputs = [['col1,col2']]
expected = []
self._test_dataset(
    inputs,
    expected,
    record_defaults=record_defaults,
    header=True,
)
