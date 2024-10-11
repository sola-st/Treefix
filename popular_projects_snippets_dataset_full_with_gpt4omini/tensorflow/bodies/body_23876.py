# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file1 = file_io.join(self._base_dir, "file1")
file_io.FileIO(file1, "wb").write("testing\n\n")
crc1 = file_io.file_crc32(file1)

file2 = file_io.join(self._base_dir, "file2")
file_io.FileIO(file2, "wb").write("testing\n\n\n")
crc2 = file_io.file_crc32(file2)

file3 = file_io.join(self._base_dir, "file3")
file_io.FileIO(file3, "wb").write("testing\n\n\n")
crc3 = file_io.file_crc32(file3)

self.assertTrue(crc1 != crc2)
self.assertEqual(crc2, crc3)
