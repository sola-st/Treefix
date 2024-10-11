# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops_test.py
# Setup a complex input pipeline.
batch_size = 2
num_epochs = 5
dataset = dataset_ops.Dataset.from_tensor_slices(
    self._createTFRecordFiles())
dataset = dataset.shuffle(buffer_size=self._num_files)
dataset = dataset.flat_map(readers.TFRecordDataset)
dataset = dataset.prefetch(buffer_size=batch_size)
dataset = dataset.shuffle(2 * self._num_files * self._num_records)
dataset = dataset.repeat(num_epochs)
dataset = dataset.map(lambda x: x)
dataset = dataset.batch(batch_size)
dataset = dataset.prefetch(buffer_size=None)

# Auto shard.
dataset = input_ops.auto_shard_dataset(
    dataset, self._num_shards, self._shard_index)

# Verify output.
next_element_fn = self._getNext(dataset)
actual = []
num_iterations = (self._num_files * self._num_records * num_epochs) // (
    self._num_shards * batch_size)
for _ in range(num_iterations):
    actual.extend(self.evaluate(next_element_fn()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(next_element_fn())

expected = []
for f in range(0, self._num_files, self._num_shards):
    for r in range(self._num_records):
        expected.append(self._record(r, f))
expected *= num_epochs

self.assertAllEqual(sorted(expected), sorted(actual))
