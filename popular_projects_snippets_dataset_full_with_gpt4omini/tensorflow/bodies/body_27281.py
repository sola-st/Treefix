# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
super(DynamicShardingFilesTest, self).setUp()
self._num_files = 5
self._num_records = 5
self._filenames = self._createFiles()
