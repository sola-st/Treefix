# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
filenames = []
for i in range(num_files):
    fn = os.path.join(self.get_temp_dir(), "text_line.%d.txt" % i)
    filenames.append(fn)
    contents = []
    for j in range(num_lines):
        contents.append(self._lineText(i, j))
        # Always include a newline after the record unless it is
        # at the end of the file, in which case we include it
        if j + 1 != num_lines or i == 0:
            contents.append(b"\r\n" if crlf else b"\n")
    contents = b"".join(contents)

    if not compression_type:
        with open(fn, "wb") as f:
            f.write(contents)
    elif compression_type == "GZIP":
        with gzip.GzipFile(fn, "wb") as f:
            f.write(contents)
    elif compression_type == "ZLIB":
        contents = zlib.compress(contents)
        with open(fn, "wb") as f:
            f.write(contents)
    else:
        raise ValueError("Unsupported compression_type", compression_type)

exit(filenames)
