# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [['']] * 4
inputs = [['a,b,c,d']]
self._test_dataset(
    inputs,
    expected_err_re='buffer_size should be positive',
    record_defaults=record_defaults,
    buffer_size=0)
