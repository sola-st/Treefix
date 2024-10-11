# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [[0]] * 4
inputs = [['1,NA,3,4', 'NA,6,7,8']]
self._test_by_comparison(
    inputs, record_defaults=record_defaults, na_value='NA')
