# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [[0.0]] * 4
inputs = [['1.0,2.1,3.2,4.3', '5.4,6.5,7.6,8.7']]
self._test_by_comparison(inputs, record_defaults=record_defaults)
