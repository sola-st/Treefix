# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
super(CacheCheckpointTest, self).setUp()
self.range_size = 10
self.num_repeats = 3
self.num_outputs = self.range_size * self.num_repeats
self.cache_file_prefix = "test"
