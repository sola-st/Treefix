# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = join(self._base_dir, "UTF8测试_file_exist")
file_io.write_string_to_file(file_path, "testing")
v = file_io.file_exists(file_path)
self.assertEqual(v, True)
