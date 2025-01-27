# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
dir_path = join(self._base_dir, "temp_dir/temp_dir1/temp_dir2")
file_io.recursive_create_dir(dir_path)
file_io.recursive_create_dir(dir_path)  # repeat creation
file_path = file_io.join(str(dir_path), "temp_file")
file_io.FileIO(file_path, mode="w").write("testing")
self.assertTrue(file_io.file_exists(file_path))
file_io.delete_recursively(file_io.join(self._base_dir, "temp_dir"))
self.assertFalse(file_io.file_exists(file_path))
