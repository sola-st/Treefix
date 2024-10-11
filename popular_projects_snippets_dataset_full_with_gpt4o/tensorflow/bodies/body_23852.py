# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
dir_path = join(self._base_dir, "test_dir")
# Failure for a non-existing dir.
self.assertFalse(file_io.is_directory(dir_path))
file_io.create_dir(dir_path)
self.assertTrue(file_io.is_directory(dir_path))
file_path = join(str(dir_path), "test_file")
file_io.FileIO(file_path, mode="w").write("test")
# False for a file.
self.assertFalse(file_io.is_directory(file_path))
# Test that the value returned from `stat()` has `is_directory` set.
file_statistics = file_io.stat(dir_path)
self.assertTrue(file_statistics.is_directory)
