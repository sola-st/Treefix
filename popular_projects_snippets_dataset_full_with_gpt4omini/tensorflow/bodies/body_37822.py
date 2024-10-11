# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
filenames = []
for i in range(self._num_files):
    fn = os.path.join(self.get_temp_dir(), "fixed_length_record.%d.txt" % i)
    filenames.append(fn)
    with open(fn, "wb") as f:
        f.write(b"H" * self._header_bytes)
        if num_records > 0:
            f.write(self._Record(i, 0))
        for j in range(1, num_records):
            if gap_bytes > 0:
                f.write(b"G" * gap_bytes)
            f.write(self._Record(i, j))
        f.write(b"F" * self._footer_bytes)
exit(filenames)
