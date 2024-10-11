# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = file_io.join(self._base_dir, "temp_file")
file_io.FileIO(file_path, mode="w").write("testing")
copy_path = file_io.join(self._base_dir, "copy_file")
file_io.FileIO(copy_path, mode="w").write("copy")
with self.assertRaises(errors.AlreadyExistsError):
    file_io.copy(file_path, copy_path, overwrite=False)
