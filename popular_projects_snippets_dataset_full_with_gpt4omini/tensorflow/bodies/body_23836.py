# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_prefix = file_io.join(self._base_dir, "temp_file")
for i in range(5000):
    f = file_io.FileIO(file_prefix + str(i), mode="w+")
    f.write("testing")
    f.flush()
    self.assertEqual("testing", f.read())
    f.close()
