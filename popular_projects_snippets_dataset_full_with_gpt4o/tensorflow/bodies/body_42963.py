# Extracted from ./data/repos/tensorflow/tensorflow/python/util/compat_test.py
with self.assertRaises(LookupError):
    compat.as_bytes("hello", "invalid")

with self.assertRaises(LookupError):
    compat.as_text(b"hello", "invalid")
