# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
super(FixedLengthRecordReaderTest, self).setUp()
self._num_files = 2
self._header_bytes = 5
self._record_bytes = 3
self._footer_bytes = 2

self._hop_bytes = 2
