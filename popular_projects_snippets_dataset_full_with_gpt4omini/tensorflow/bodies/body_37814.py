# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
filenames = []
for i in range(self._num_files):
    fn = os.path.join(self.get_temp_dir(), "text_line.%d.txt" % i)
    filenames.append(fn)
    with open(fn, "wb") as f:
        for j in range(self._num_lines):
            f.write(self._LineText(i, j))
            # Always include a newline after the record unless it is
            # at the end of the file, in which case we include it sometimes.
            if j + 1 != self._num_lines or i == 0:
                f.write(b"\r\n" if crlf else b"\n")
exit(filenames)
