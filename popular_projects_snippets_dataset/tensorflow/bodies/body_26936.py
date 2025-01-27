# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [['']] * 4
inputs = [['"a","b","c :)","d"', '"e","f","g :(","h"']]
self._test_by_comparison(inputs, record_defaults=record_defaults)
