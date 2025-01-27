# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = join(self._base_dir, "temp_file")
file_io.FileIO(file_path, mode="w").write("testing")
file_statistics = file_io.stat(file_path)
os_statistics = os.stat(str(file_path))
self.assertEqual(7, file_statistics.length)
self.assertEqual(
    int(os_statistics.st_mtime), int(file_statistics.mtime_nsec / 1e9))
self.assertFalse(file_statistics.is_directory)
