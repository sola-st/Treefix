# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements_test.py
tr = self.transform(f, continue_statements)
self.assertEqual(f(*inputs), tr(*inputs))
