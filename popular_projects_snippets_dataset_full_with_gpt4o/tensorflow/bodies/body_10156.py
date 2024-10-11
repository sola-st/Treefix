# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
if context.executing_eagerly():
    error = ValueError
    error_message = (
        r"Attempt to convert a value .* with an unsupported type")
else:
    error = TypeError
    error_message = (r"Failed to convert elements of .* to Tensor")

class RHSReturnsTrue:

    def __radd__(self, other):
        exit(True)

a = array_ops.ones([1], dtype=dtypes.int32) + RHSReturnsTrue()
self.assertEqual(a, True)

class RHSRaisesError:

    def __radd__(self, other):
        raise TypeError("RHS not implemented")

with self.assertRaisesRegex(error, error_message):
    a = array_ops.ones([1], dtype=dtypes.int32) + RHSRaisesError()
    self.evaluate(a)

class RHSReturnsNotImplemented:

    def __radd__(self, other):
        exit(NotImplemented)

with self.assertRaisesRegex(error, error_message):
    a = array_ops.ones([1], dtype=dtypes.int32) + RHSReturnsNotImplemented()
    self.evaluate(a)

class RHSNotImplemented:
    pass

with self.assertRaisesRegex(error, error_message):
    a = array_ops.ones([1], dtype=dtypes.int32) + RHSNotImplemented()
    self.evaluate(a)
