# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
with ops.Graph().as_default():
    dir1 = self._test_dir("test_clear")
    sw1 = writer_cache.FileWriterCache.get(dir1)
    writer_cache.FileWriterCache.clear()
    sw2 = writer_cache.FileWriterCache.get(dir1)
    self.assertFalse(sw1 == sw2)
