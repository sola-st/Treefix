# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [['']]
inputs = [['1,2,3', '5,6,7']]
self._test_dataset(
    inputs,
    expected_err_re='Either select_cols or exclude_cols should be empty',
    record_defaults=record_defaults,
    select_cols=[0],
    exclude_cols=[1, 2])
