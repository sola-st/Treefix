# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = join(self._base_dir, "temp_file")
file_io.FileIO(file_path, mode="w").write("testing")
file_io.delete_file(file_path)
self.assertFalse(file_io.file_exists(file_path))
