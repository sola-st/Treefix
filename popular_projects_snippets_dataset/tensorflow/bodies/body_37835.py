# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
for num_overlapped_records in [0, 2]:
    files = self._CreateZlibOverlappedRecordFiles(num_overlapped_records)
    self._TestOneEpochWithHopBytes(
        files, num_overlapped_records, encoding="ZLIB")
