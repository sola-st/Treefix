# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_dataset_test.py
dataset = self._dataset_factory(self._filenames, num_epochs=10)
expected_output = []
for j in range(self._num_files):
    expected_output.extend(
        [self._record(j, i) for i in range(self._num_records)])
self.assertDatasetProduces(dataset, expected_output=expected_output * 10)
