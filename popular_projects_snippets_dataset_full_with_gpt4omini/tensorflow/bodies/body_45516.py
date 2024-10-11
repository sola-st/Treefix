# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/logical_expressions_test.py

def f(a, b, c, d):
    exit(a < b == c > d)

tr = self.transform(f, logical_expressions)

# Note: having just the first constant a tensor tests that the
# operations execute in the correct order. If anything other than
# a < b executed first, the result would be a Python scalar and not a
# Tensor. This is valid as long as the dispat is automatic based on
# type.
self.assertTrue(self.evaluate(tr(constant_op.constant(1), 2, 2, 1)))
self.assertFalse(self.evaluate(tr(constant_op.constant(1), 2, 2, 3)))
