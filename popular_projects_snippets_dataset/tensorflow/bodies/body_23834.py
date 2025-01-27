# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = join(self._base_dir, "temp_file")
file_io.FileIO(file_path, "wb").write("testing")
with file_io.FileIO(file_path, mode="r") as f:
    self.assertEqual("testing", f.read())
