# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops_test.py
dataset1 = readers.TFRecordDataset(self._createTFRecordFiles())
dataset2 = readers.TextLineDataset(self._createTextFiles())

dataset = dataset_ops.Dataset.zip((dataset1, dataset2))
dataset = input_ops.auto_shard_dataset(
    dataset, self._num_shards, self._shard_index)

record_fn = lambda r, f: (self._record(r, f), self._text_line(r, f))
self._verifySimpleShardingOutput(dataset, record_fn)
