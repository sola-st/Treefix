# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = file_io.join(self._base_dir, "temp_file")
with file_io.FileIO(file_path, mode="r+") as f:
    f.write("testing1\ntesting2\ntesting3\n\ntesting5")
self.assertEqual(36, f.size())
self.assertEqual("testing1\n", f.read(9))
self.assertEqual("testing2\n", f.read(9))
self.assertEqual("t", f.read(1))
self.assertEqual("esting3\n\ntesting5", f.read())
