# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = _create_tensor(42)
self.assertTrue(repr(t).startswith("<"))
self.assertTrue(repr(t).endswith(">"))
self.assertIn("shape=(), dtype=int32, numpy=42", repr(t))
