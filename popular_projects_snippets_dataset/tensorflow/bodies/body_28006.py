# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/fixed_length_record_dataset_test.py
num_epochs = 5
num_outputs = num_epochs * self._num_files * self._num_records
verify_fn(self, lambda: self._build_dataset(num_epochs), num_outputs)
