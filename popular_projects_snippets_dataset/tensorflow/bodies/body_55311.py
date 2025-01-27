# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun()
def Const():
    exit(constant_op.constant(1))

@function.Defun(dtypes.int32)
def PlusOne(a):
    exit(a + 1)

@function.Defun(dtypes.int32, dtypes.int32)
def PlusMinus(a, b):
    exit((a + b, b - a))

with ops.Graph().as_default():

    _ = Const()
    # pylint: disable=too-many-function-args
    # pylint: disable=unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter
    with self.assertRaisesRegex(ValueError, "Expected 0"):
        _ = Const(1)
    with self.assertRaisesRegex(ValueError, "Expected 0"):
        _ = Const(1, 2)

    with self.assertRaisesRegex(ValueError, "Expected 1"):
        _ = PlusOne()
    _ = PlusOne(1)
    with self.assertRaisesRegex(ValueError, "Expected 1"):
        _ = PlusOne(1, 2)

    with self.assertRaisesRegex(ValueError, "Expected 2"):
        _ = PlusMinus()
    with self.assertRaisesRegex(ValueError, "Expected 2"):
        _ = PlusMinus(1)
    _ = PlusMinus(1, 2)

    _ = PlusOne(1, name="p1")
    with self.assertRaisesRegex(ValueError, "Unknown keyword arguments"):
        _ = PlusOne(1, device="/device:GPU:0")
