# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
for fn in self._filenames:
    os.remove(fn)
super(WholeFileReaderTest, self).tearDown()
