# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops_test.py
dataset1 = readers.TFRecordDataset(self._createTFRecordFiles())
dataset2 = readers.TextLineDataset(self._createTextFiles())

dataset = dataset1.concatenate(dataset2)
dataset = input_ops.auto_shard_dataset(
    dataset, self._num_shards, self._shard_index)

next_element_fn = self._getNext(dataset)
for f in range(self._shard_index, self._num_files, self._num_shards):
    for r in range(self._num_records):
        self.assertAllEqual(
            self._record(r, f), self.evaluate(next_element_fn()))
for f in range(self._shard_index, self._num_files, self._num_shards):
    for r in range(self._num_records):
        self.assertAllEqual(
            self._text_line(r, f), self.evaluate(next_element_fn()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(next_element_fn())
