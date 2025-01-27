# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/fixed_length_record_dataset_test.py
test_filenames = self._createFiles()
dataset = readers.FixedLengthRecordDataset(
    test_filenames,
    self._record_bytes,
    self._header_bytes,
    self._footer_bytes,
    name="fixed_length_record_dataset")
expected_output = []
for j in range(self._num_files):
    expected_output.extend(
        [self._record(j, i) for i in range(self._num_records)])
self.assertDatasetProduces(dataset, expected_output=expected_output)
