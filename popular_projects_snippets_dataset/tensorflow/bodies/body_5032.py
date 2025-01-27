# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops_test.py
super(AutoShardDatasetTest, self).setUp()
self._num_files = 10
self._num_records = 4
self._num_shards = 2
self._shard_index = 0
self._record_bytes = 10
