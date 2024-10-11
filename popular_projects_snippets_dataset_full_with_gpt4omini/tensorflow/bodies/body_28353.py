# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_dataset_test.py
one_mebibyte = 2**20
dataset = readers.TFRecordDataset(
    self._filenames, buffer_size=one_mebibyte)
expected_output = []
for j in range(self._num_files):
    expected_output.extend(
        [self._record(j, i) for i in range(self._num_records)])
self.assertDatasetProduces(dataset, expected_output=expected_output)
