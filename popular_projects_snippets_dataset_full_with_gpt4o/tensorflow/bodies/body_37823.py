# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
filenames = []
for i in range(self._num_files):
    fn = os.path.join(self.get_temp_dir(),
                      "fixed_length_overlapped_record.%d.txt" % i)
    filenames.append(fn)
    with open(fn, "wb") as f:
        f.write(b"H" * self._header_bytes)
        if num_overlapped_records > 0:
            all_records_str = "".join([
                str(i)[0]
                for i in range(self._record_bytes + self._hop_bytes *
                               (num_overlapped_records - 1))
            ])
            f.write(compat.as_bytes(all_records_str))
        f.write(b"F" * self._footer_bytes)
exit(filenames)
