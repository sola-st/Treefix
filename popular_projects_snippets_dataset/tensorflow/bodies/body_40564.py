# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
x = value_fn()
self.assertIsInstance(int(x), int)
self.assertEqual(int(x), 1)
self.assertIsInstance(float(x), float)
self.assertAllClose(float(x), 1.3)
self.assertIsInstance(complex(x), complex)
self.assertAllClose(complex(x), 1.3+1j)
