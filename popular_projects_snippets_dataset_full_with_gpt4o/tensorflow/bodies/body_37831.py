# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
for num_records in [0, 7]:
    # gap_bytes=0: hop_bytes=0
    # gap_bytes=1: hop_bytes=record_bytes+1
    for gap_bytes in [0, 1]:
        files = self._CreateGzipFiles(num_records, gap_bytes)
        self._TestOneEpoch(files, num_records, gap_bytes, encoding="GZIP")
