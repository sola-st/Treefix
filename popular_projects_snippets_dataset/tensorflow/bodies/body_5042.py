# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(
    self._createTFRecordFiles())
dataset = dataset.flat_map(readers.TFRecordDataset)
dataset = input_ops.auto_shard_dataset(
    dataset, self._num_shards, self._shard_index)

self._verifySimpleShardingOutput(dataset, self._record)
