# Extracted from ./data/repos/tensorflow/tensorflow/python/util/compat_test.py
self.assertEqual(compat.as_bytes("hello", "utf8"), b"hello")
self.assertEqual(compat.as_text(b"hello", "utf-8"), "hello")
