# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
super(WholeFileReaderTest, self).setUp()
self._filenames = [
    os.path.join(self.get_temp_dir(), "whole_file.%d.txt" % i)
    for i in range(3)
]
self._content = [b"One\na\nb\n", b"Two\nC\nD", b"Three x, y, z"]
for fn, c in zip(self._filenames, self._content):
    with open(fn, "wb") as h:
        h.write(c)
