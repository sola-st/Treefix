# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
"""file_io.join respects the os.path.join behavior for native filesystems."""
for sep in ("/", "\\", os.sep):
    self.assertEqual(os.path.join("a", "b", "c"), file_io.join("a", "b", "c"))
    self.assertEqual(
        os.path.join(sep + "a", "b", "c"), file_io.join(sep + "a", "b", "c"))
    self.assertEqual(
        os.path.join("a", sep + "b", "c"), file_io.join("a", sep + "b", "c"))
    self.assertEqual(
        os.path.join("a", "b", sep + "c"), file_io.join("a", "b", sep + "c"))
    self.assertEqual(
        os.path.join("a", "b", "c" + sep), file_io.join("a", "b", "c" + sep))
