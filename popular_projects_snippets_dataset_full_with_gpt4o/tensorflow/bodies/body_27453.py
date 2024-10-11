# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
super(AutoShardDatasetTest, self).setUp()
self._num_files = 10
self._num_records = 10
self._filenames = self._createFiles()
