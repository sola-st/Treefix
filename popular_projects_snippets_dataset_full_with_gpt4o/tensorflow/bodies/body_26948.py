# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
# Testing reading with a range of buffer sizes that should all work.
for i in list(range(1, 1 + num_sizes_to_test)) + [None]:
    self._test_dataset(
        inputs,
        expected,
        linebreak=linebreak,
        compression_type=compression_type,
        record_defaults=record_defaults,
        buffer_size=i)
