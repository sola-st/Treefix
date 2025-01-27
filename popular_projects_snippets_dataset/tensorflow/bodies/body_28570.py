# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
super(FileCacheTest, self).setUp()
self.tmp_dir = tempfile.mkdtemp()
self.cache_prefix = path.join(self.tmp_dir, "cache")
