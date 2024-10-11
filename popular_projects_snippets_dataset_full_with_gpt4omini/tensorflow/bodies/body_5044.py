# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops_test.py
filenames = self._createTFRecordFiles()
file_pattern = filenames[0].rsplit(os.sep, 1)[0] + "/tf_record.*.txt"
dataset = dataset_ops.Dataset.list_files(file_pattern, shuffle=False)
dataset = dataset.flat_map(readers.TFRecordDataset)
dataset = input_ops.auto_shard_dataset(
    dataset, self._num_shards, self._shard_index)

next_element_fn = self._getNext(dataset)
actual, expected = [], []
for f in range(self._shard_index, self._num_files, self._num_shards):
    for r in range(self._num_records):
        actual.append(self.evaluate(next_element_fn()))
        expected.append(self._record(r, f))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(next_element_fn())
self.assertAllEqual(expected, actual)
