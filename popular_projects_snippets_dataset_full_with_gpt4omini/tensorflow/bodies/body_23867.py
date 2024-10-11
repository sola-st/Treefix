# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = file_io.join(self._base_dir, "temp_file")
data = ["testing1\n", "testing2\n", "testing3\n", "\n", "testing5"]
f = file_io.FileIO(file_path, mode="r+")
f.write("".join(data))
f.flush()
lines = f.readlines()
self.assertSequenceEqual(lines, data)
