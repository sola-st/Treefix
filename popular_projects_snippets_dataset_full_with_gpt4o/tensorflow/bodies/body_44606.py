# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/variables_test.py
self.assertEqual(variables.ld(1), 1)
o = object()
self.assertEqual(variables.ld(o), o)

self.assertIsNone(variables.ld(None))
