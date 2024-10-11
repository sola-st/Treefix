# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(
    self._createTFRecordFiles())
dataset = dataset.interleave(
    readers.TFRecordDataset, cycle_length=4, block_length=self._num_records)
dataset = input_ops.auto_shard_dataset(
    dataset, self._num_shards, self._shard_index)

# Since block_length == num records in each file, the output will still
# contain records in order of files.
self._verifySimpleShardingOutput(dataset, self._record)
