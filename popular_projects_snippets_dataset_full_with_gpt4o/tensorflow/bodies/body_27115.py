# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
num_repeats = 4
num_outputs = num_repeats * 2
verify_fn(self, lambda: self._build_dataset(num_repeats), num_outputs)
