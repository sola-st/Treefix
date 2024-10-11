# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [['']]
inputs = [['1,2,3', '5,6,7']]
self._test_dataset(
    inputs,
    expected_output=[['1'], ['5']],
    record_defaults=record_defaults,
    exclude_cols=[1, 2])
