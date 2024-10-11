# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = file_io.join(self._base_dir, "temp_file")
with file_io.FileIO(file_path, mode="w") as f:
    f.write("begin\n")
with file_io.FileIO(file_path, mode="a") as f:
    f.write("a1\n")
with file_io.FileIO(file_path, mode="a") as f:
    f.write("a2\n")
with file_io.FileIO(file_path, mode="r") as f:
    file_contents = f.read()
    self.assertEqual("begin\na1\na2\n", file_contents)
