# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = join(self._base_dir, "temp_file")
file_io.write_string_to_file(file_path, "testing")
with file_io.FileIO(file_path, mode="rb") as f:
    self.assertEqual(b"testing", f.read())
