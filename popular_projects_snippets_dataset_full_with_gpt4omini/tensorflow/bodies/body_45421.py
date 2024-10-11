# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py
tr = self.transform(f, (functions, return_statements))
self.assertEqual(f(*inputs), tr(*inputs))
