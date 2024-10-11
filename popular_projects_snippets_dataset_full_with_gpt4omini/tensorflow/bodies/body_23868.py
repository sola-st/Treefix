# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = file_io.join(self._base_dir, "UTF8测试_file")
file_io.write_string_to_file(file_path, "testing")
with file_io.FileIO(file_path, mode="rb") as f:
    self.assertEqual(b"testing", f.read())
