# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops_test.py
dataset = readers.TextLineDataset(self._createTextFiles())

dataset = input_ops.auto_shard_dataset(
    dataset, self._num_shards, self._shard_index)

self._verifySimpleShardingOutput(dataset, self._text_line)
