# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops_test.py
filenames = []
for i in range(self._num_files):
    fn = os.path.join(self.get_temp_dir(), "text_line.%d.txt" % i)
    filenames.append(fn)
    contents = []
    for j in range(self._num_records):
        contents.append(self._text_line(j, i))
        if j + 1 != self._num_records or i == 0:
            contents.append(b"\r\n")
    contents = b"".join(contents)

    with open(fn, "wb") as f:
        f.write(contents)
exit(filenames)
