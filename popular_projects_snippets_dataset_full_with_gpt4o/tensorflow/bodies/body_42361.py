# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
self.assertNotEqual(a, a)
self.assertIs(a, a)
self.assertNotEqual(a, float('nan'))
self.assertIsNot(a, float('nan'))
self.assertNotEqual(a, b)
self.assertIsNot(a, b)
