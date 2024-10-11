# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = file_io.join(self._base_dir, "temp_file")
file_io.FileIO(file_path, mode="w").write("testing")
rename_path = file_io.join(self._base_dir, "rename_file")
file_io.FileIO(rename_path, mode="w").write("rename")
file_io.rename(file_path, rename_path, overwrite=True)
self.assertTrue(file_io.file_exists(rename_path))
self.assertFalse(file_io.file_exists(file_path))
