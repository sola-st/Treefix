# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
# Testing using dtypes as record_defaults for required fields
record_defaults = [dtypes.float32, [0.0]]
inputs = [['1.0,2.0', '3.0,4.0']]
self._test_dataset(
    inputs,
    [[1.0, 2.0], [3.0, 4.0]],
    record_defaults=record_defaults,
)
