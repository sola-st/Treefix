# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
if self.tmp_dir:
    shutil.rmtree(self.tmp_dir, ignore_errors=True)
super(FileCacheTest, self).tearDown()
