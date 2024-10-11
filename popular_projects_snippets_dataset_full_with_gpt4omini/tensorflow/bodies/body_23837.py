# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = file_io.join(self._base_dir, "temp_file")
with file_io.FileIO(file_path, mode="w") as f:
    f.write("line1\n")
    f.write("line2")
file_contents = file_io.read_file_to_string(file_path)
self.assertEqual("line1\nline2", file_contents)
