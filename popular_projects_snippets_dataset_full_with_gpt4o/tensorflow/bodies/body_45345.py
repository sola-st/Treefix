# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/list_comprehensions_test.py
tr = self.transform(f, list_comprehensions)
self.assertEqual(f(*inputs), tr(*inputs))
