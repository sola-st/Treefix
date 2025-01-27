# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = join(self._base_dir, "temp_file")
file_io.FileIO(file_path, mode="w").write("testing")
copy_path = join(self._base_dir, "copy_file")
file_io.copy(file_path, copy_path)
self.assertTrue(file_io.file_exists(copy_path))
f = file_io.FileIO(file_path, mode="r")
self.assertEqual("testing", f.read())
self.assertEqual(7, f.tell())
