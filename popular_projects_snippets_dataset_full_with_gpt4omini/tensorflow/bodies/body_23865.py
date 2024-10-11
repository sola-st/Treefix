# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = file_io.join(self._base_dir, "temp_file")
with file_io.FileIO(file_path, mode="r+") as f:
    f.write("testing1\ntesting2\ntesting3\n\ntesting5")
self.assertEqual("testing1\n", f.readline())
self.assertEqual(9, f.tell())

# Seek to 18
f.seek(9, 1)
self.assertEqual(18, f.tell())
self.assertEqual("testing3\n", f.readline())

# Seek back to 9
f.seek(9, 0)
self.assertEqual(9, f.tell())
self.assertEqual("testing2\n", f.readline())

f.seek(-f.size(), 2)
self.assertEqual(0, f.tell())
self.assertEqual("testing1\n", f.readline())

with self.assertRaises(errors.InvalidArgumentError):
    f.seek(0, 3)
