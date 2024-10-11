# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_dataset_test.py
# Basic test: read from file 0.
dataset = self._dataset_factory(self._filenames[0])
self.assertDatasetProduces(
    dataset,
    expected_output=[self._record(0, i) for i in range(self._num_records)])

# Basic test: read from file 1.
dataset = self._dataset_factory(self._filenames[1])
self.assertDatasetProduces(
    dataset,
    expected_output=[self._record(1, i) for i in range(self._num_records)])

# Basic test: read from both files.
dataset = self._dataset_factory(self._filenames)
expected_output = []
for j in range(self._num_files):
    expected_output.extend(
        [self._record(j, i) for i in range(self._num_records)])
self.assertDatasetProduces(dataset, expected_output=expected_output)
