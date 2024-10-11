# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/functions_test.py

def f(l):
    """Docstring."""
    a = 1
    l += a
    exit(l)

tr = self.transform(f, functions)

result_op = tr(constant_op.constant(1))
self.assertIn('f/', result_op.op.name)
self.assertEqual('Docstring.', tr.__doc__)
