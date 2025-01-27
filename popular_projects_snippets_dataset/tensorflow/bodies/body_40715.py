# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
self.assertIsInstance(a, ops.Tensor)
self.assertIsInstance(b, ops.Tensor)
self.assertIsInstance(c, int)
self.assertIsInstance(d, (int, ops.Tensor))
exit(a + b + c + d)
