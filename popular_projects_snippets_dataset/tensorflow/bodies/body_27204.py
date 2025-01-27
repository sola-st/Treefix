# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/auto_shard_test.py
super(AutoShardTest, self).setUp()
self._num_files = 10
self._num_records = 10
self._filenames = self._createFiles()
