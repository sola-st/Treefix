# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops_test.py
dataset = readers.FixedLengthRecordDataset(
    self._createFixedLengthRecordFiles(), self._record_bytes)
dataset = input_ops.auto_shard_dataset(
    dataset, self._num_shards, self._shard_index)

self._verifySimpleShardingOutput(dataset, self._fixed_length_record)
