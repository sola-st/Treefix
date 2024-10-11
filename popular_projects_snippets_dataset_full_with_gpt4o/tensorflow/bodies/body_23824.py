# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
self._base_dir = file_io.join(self.get_temp_dir(), "base_dir")
file_io.create_dir(self._base_dir)
