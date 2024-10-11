# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file1 = file_io.join(self._base_dir, "file1")
file_io.write_string_to_file(file1, "This is a sentence\n" * 100)
crc1 = file_io.file_crc32(file1)

file2 = file_io.join(self._base_dir, "file2")
file_io.write_string_to_file(file2, "This is another sentence\n" * 100)
crc2 = file_io.file_crc32(file2)

file3 = file_io.join(self._base_dir, "file3")
file_io.write_string_to_file(file3, "This is another sentence\n" * 100)
crc3 = file_io.file_crc32(file3)

self.assertTrue(crc1 != crc2)
self.assertEqual(crc2, crc3)
