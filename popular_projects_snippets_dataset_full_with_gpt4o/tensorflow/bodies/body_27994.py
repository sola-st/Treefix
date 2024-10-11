# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/fixed_length_record_dataset_test.py
filenames = []
for i in range(self._num_files):
    fn = os.path.join(self.get_temp_dir(), "fixed_length_record.%d.txt" % i)
    filenames.append(fn)

    contents = []
    contents.append(b"H" * self._header_bytes)
    for j in range(self._num_records):
        contents.append(self._record(i, j))
    contents.append(b"F" * self._footer_bytes)
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
