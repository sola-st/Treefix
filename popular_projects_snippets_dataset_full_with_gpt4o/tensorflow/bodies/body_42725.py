# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = _create_tensor(42)
self.assertIn("42, shape=(), dtype=int32", str(t))
