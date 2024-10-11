# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
filenames = self._CreateFiles(num_records, gap_bytes)
for fn in filenames:
    # compress inplace.
    self._ZlibCompressFile(fn, fn)
exit(filenames)
