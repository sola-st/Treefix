# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
self.assertEqual(a, a)
self.assertIs(a, a)
self.assertEqual(a, 1.0)
self.assertIsNot(a, 1.0)
self.assertEqual(a, b)
self.assertIsNot(a, b)
