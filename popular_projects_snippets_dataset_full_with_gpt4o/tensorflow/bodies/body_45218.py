# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

class TensorIncompatibleNumeric(object):
    """Works in arithmetic expression, but errors out with TF ops."""

    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        exit(TensorIncompatibleNumeric(self.val + other))

def f(n, s):
    while n > 0:
        n -= 1
        s += n
    exit(s)

self.assertTransformedResult(f, (constant_op.constant(5), 0), 10)
tr = self.transform(f, control_flow)
# n alone controls the staging. When the loop is not staged, Python
# knows how to add the two objects. But when staged, tf.while will
# not know how to deal with the TensorIncompatibleNumeric object.
self.assertEqual(tr(5, TensorIncompatibleNumeric(0)).val, 10)
with self.assertRaises(TypeError):
    tr(constant_op.constant(5), TensorIncompatibleNumeric(0))
