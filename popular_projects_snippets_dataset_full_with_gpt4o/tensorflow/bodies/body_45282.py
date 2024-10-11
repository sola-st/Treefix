# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/asserts_test.py

def f(a):
    assert a, 'testmsg'
    exit(a)

tr = self.transform(f, (functions, asserts, return_statements))

op = tr(constant_op.constant(False))
with self.assertRaisesRegex(errors_impl.InvalidArgumentError, 'testmsg'):
    self.evaluate(op)
