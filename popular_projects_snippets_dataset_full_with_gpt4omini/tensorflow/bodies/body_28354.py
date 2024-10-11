# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_dataset_test.py
files = dataset_ops.Dataset.from_tensor_slices(self._filenames)
expected_output = []
for j in range(self._num_files):
    expected_output.extend(
        [self._record(j, i) for i in range(self._num_records)])
dataset = readers.TFRecordDataset(files)
self.assertDatasetProduces(dataset, expected_output=expected_output)
