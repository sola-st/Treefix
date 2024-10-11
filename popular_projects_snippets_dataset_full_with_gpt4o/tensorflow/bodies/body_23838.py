# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = file_io.join(self._base_dir, "temp_file")
with self.assertRaises(errors.PermissionDeniedError):
    file_io.FileIO(file_path, mode="r").write("testing")
