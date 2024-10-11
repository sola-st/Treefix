# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = file_io.join(self._base_dir, "temp_file")
with open(file_path, mode="w", encoding="cp932") as f:
    f.write("今日はいい天気")
with file_io.FileIO(file_path, mode="r", encoding="cp932") as f:
    self.assertEqual(f.read(), "今日はいい天気")

with file_io.FileIO(file_path, mode="w", encoding="cp932") as f:
    f.write("今日はいい天気")
with open(file_path, mode="r", encoding="cp932") as f:
    self.assertEqual(f.read(), "今日はいい天気")
