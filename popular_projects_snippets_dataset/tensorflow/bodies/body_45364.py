# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/break_statements_test.py
tr = self.transform(f, break_statements)
self.assertEqual(f(*inputs), tr(*inputs))
