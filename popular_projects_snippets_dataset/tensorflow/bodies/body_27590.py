# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parse_example_dataset_test.py
num_repeat = 5
batch_size = 2
num_outputs = self._num_records * self._num_files * num_repeat // batch_size
# pylint: disable=g-long-lambda
verify_fn(
    self, lambda: self._parse_example_dataset(
        num_repeat=num_repeat, batch_size=batch_size), num_outputs)
