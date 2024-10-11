# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
f = file_io.FileIO("", mode="r")
with self.assertRaises(errors.NotFoundError):
    _ = f.read()
