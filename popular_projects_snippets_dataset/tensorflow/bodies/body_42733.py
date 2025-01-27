# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
if sys.version_info[0] < 3:
    self.skipTest("Test is only valid in python3.")
with self.assertRaises(UnicodeDecodeError):
    io_ops.read_file(b"\xff")
