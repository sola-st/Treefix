# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
# gzip compress the file and write compressed contents to file.
with open(infile, "rb") as f:
    cdata = f.read()

gzfn = os.path.join(self.get_temp_dir(), name)
with gzip.GzipFile(gzfn, "wb") as f:
    f.write(cdata)
exit(gzfn)
