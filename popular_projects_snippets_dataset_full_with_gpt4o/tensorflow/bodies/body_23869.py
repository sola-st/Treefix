# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
"""Test that reading past EOF does not raise an exception."""

file_path = file_io.join(self._base_dir, "temp_file")
f = file_io.FileIO(file_path, mode="r+")
content = "testing"
f.write(content)
f.flush()
self.assertEqual(content, f.read(len(content) + 1))
