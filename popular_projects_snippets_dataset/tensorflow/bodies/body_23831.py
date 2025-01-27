# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = file_io.join(self._base_dir, "temp_file")
file_io.atomic_write_string_to_file(file_path, "testing")
self.assertTrue(file_io.file_exists(file_path))
file_contents = file_io.read_file_to_string(file_path)
self.assertEqual("testing", file_contents)
