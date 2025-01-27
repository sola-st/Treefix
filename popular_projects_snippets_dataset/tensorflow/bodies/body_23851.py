# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
fake_dir_path = file_io.join(self._base_dir, "temp_dir")
with self.assertRaises(errors.NotFoundError):
    file_io.delete_recursively(fake_dir_path)
