# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_dataset_test.py
num_epochs = 5
num_outputs = num_epochs * self._num_files * self._num_records
# pylint: disable=g-long-lambda
verify_fn(
    self, lambda: self.make_dataset(
        num_epochs, compression_type=compression_type), num_outputs)
