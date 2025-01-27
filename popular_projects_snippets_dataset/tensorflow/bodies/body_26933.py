# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [['']] * 2
inputs = [['', '1,2']]  # First record is empty
self._test_dataset(
    inputs,
    expected_err_re='Expect 2 fields but have 1 in record',
    record_defaults=record_defaults)
