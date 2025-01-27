# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
"""file_io.join joins url-like filesystems with '/' on all platform."""
for fs in ("ram://", "gcs://", "file://"):
    expected = fs + "exists/a/b/c.txt"
    self.assertEqual(file_io.join(fs, "exists", "a", "b", "c.txt"), expected)
    self.assertEqual(file_io.join(fs + "exists", "a", "b", "c.txt"), expected)
    self.assertEqual(file_io.join(fs, "exists/a", "b", "c.txt"), expected)
    self.assertEqual(file_io.join(fs, "exists", "a", "b/c.txt"), expected)
