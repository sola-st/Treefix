# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
dir_path = file_io.join(self._base_dir, "test_dir")
with self.assertRaises(errors.NotFoundError):
    file_io.list_directory(dir_path)
