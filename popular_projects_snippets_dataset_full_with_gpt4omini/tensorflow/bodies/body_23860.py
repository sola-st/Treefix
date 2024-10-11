# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = file_io.join(self._base_dir, "temp_file")
with file_io.FileIO(file_path, mode="r+") as f:
    f.write("testing1\ntesting2\ntesting3\n\ntesting5")
self.assertEqual(36, f.size())
self.assertEqual("testing1\n", f.readline())
self.assertEqual("testing2\n", f.readline())
self.assertEqual("testing3\n", f.readline())
self.assertEqual("\n", f.readline())
self.assertEqual("testing5", f.readline())
self.assertEqual("", f.readline())
