# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = join(self._base_dir, "temp_file")
self.assertFalse(file_io.file_exists(file_path))
with self.assertRaises(errors.NotFoundError):
    _ = file_io.read_file_to_string(file_path)
