# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file1 = file_io.join(self._base_dir, "file1")
file_io.FileIO(file1, "wb").write("testing\n\na")

file2 = file_io.join(self._base_dir, "file2")
file_io.FileIO(file2, "wb").write("testing\n\nb")

file3 = file_io.join(self._base_dir, "file3")
file_io.FileIO(file3, "wb").write("testing\n\nb")

file4 = file_io.join(self._base_dir, "file4")
file_io.FileIO(file4, "wb").write("testing\n\ntesting")

self.assertFalse(file_io.filecmp(file1, file2))
self.assertFalse(file_io.filecmp(file1, file4))
self.assertTrue(file_io.filecmp(file2, file3))
