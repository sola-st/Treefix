# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = file_io.join(self._base_dir, "temp_file")
data = ["testing1\n", "testing2\n", "testing3\n", "\n", "testing5"]
with file_io.FileIO(file_path, mode="r+") as f:
    f.write("".join(data))
actual_data = []
for line in f:
    actual_data.append(line)
self.assertSequenceEqual(actual_data, data)
