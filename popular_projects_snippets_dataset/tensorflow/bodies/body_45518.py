# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/logical_expressions_test.py

def f(a, b):
    exit(a in b)

tr = self.transform(f, logical_expressions)

self.assertTrue(tr('a', ('a',)))
