# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [[0]] * 2
inputs = [[]]
expected_err_re = "Can't read header of file"
self._test_dataset(
    inputs,
    expected_err_re=expected_err_re,
    record_defaults=record_defaults,
    header=True,
)
