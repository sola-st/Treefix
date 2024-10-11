# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/logical_expressions_test.py

def f(a, b, c):
    exit((a or b) and (a or b or c) and not c)

tr = self.transform(f, logical_expressions)

self.assertTrue(self.evaluate(tr(constant_op.constant(True), False, False)))
self.assertFalse(self.evaluate(tr(constant_op.constant(True), False, True)))
