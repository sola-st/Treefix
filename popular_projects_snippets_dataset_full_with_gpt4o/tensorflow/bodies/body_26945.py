# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [['']] * 4
inputs = [['a,b,c,"a']]
self._test_dataset(
    inputs,
    expected_err_re=
    'Reached end of file without closing quoted field in record',
    record_defaults=record_defaults)
