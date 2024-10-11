# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file1 = file_io.join(self._base_dir, "file1")
file_io.write_string_to_file(file1, "This is a sentence\n" * 100)

file2 = file_io.join(self._base_dir, "file2")
file_io.write_string_to_file(file2, "This is b sentence\n" * 100)

file3 = file_io.join(self._base_dir, "file3")
file_io.write_string_to_file(file3, u"This is b sentence\n" * 100)

self.assertFalse(file_io.filecmp(file1, file2))
self.assertTrue(file_io.filecmp(file2, file3))
