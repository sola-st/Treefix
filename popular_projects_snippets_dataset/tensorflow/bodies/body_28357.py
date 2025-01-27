# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_dataset_test.py
files = [self._filenames[0]]

expected_output = [self._record(0, i) for i in range(self._num_records)]
ds = readers.TFRecordDataset(files, name="tf_record_dataset")
self.assertDatasetProduces(
    ds, expected_output=expected_output, assert_items_equal=True)
