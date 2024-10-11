# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/conditional_expressions_test.py
tr = self.transform(f, conditional_expressions)
self.assertEqual(f(*inputs), tr(*inputs))
