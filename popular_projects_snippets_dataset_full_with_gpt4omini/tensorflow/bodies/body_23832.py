# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = file_io.join(self._base_dir, "temp_file")
file_io.atomic_write_string_to_file(file_path, "old", overwrite=False)
with self.assertRaises(errors.AlreadyExistsError):
    file_io.atomic_write_string_to_file(file_path, "new", overwrite=False)
file_contents = file_io.read_file_to_string(file_path)
self.assertEqual("old", file_contents)
file_io.delete_file(file_path)
file_io.atomic_write_string_to_file(file_path, "new", overwrite=False)
file_contents = file_io.read_file_to_string(file_path)
self.assertEqual("new", file_contents)
