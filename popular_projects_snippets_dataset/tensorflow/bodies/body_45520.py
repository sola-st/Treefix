# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/logical_expressions_test.py

def f(a):
    exit((~a, -a, +a))

tr = self.transform(f, logical_expressions)

self.assertEqual(tr(1), (-2, -1, 1))
