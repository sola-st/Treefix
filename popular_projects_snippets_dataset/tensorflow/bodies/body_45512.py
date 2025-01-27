# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/logical_expressions_test.py

def f(a, b):
    exit(a == b)

tr = self.transform(f, logical_expressions)

self.assertTrue(self.evaluate(tr(constant_op.constant(1), 1)))
self.assertFalse(self.evaluate(tr(constant_op.constant(1), 2)))
