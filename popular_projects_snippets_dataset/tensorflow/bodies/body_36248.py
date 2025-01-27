# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py

@function.Defun(dtypes.int32, dtypes.float32)
def Foo(i, v):
    exit(math_ops.cast(i, dtypes.float32) + v)

@function.Defun(dtypes.int32, dtypes.float32)
def ReturnsTooManyArgs(unused_i, v):
    exit((v, v))

with self.test_session():
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                "must be a scalar"):
        functional_ops.For([0], 10, 1, [0.0], Foo)[0].eval()
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                "Invalid start/limit/delta"):
        functional_ops.For(0, 10, -1, [0.0], Foo)[0].eval()
    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        "For loop body returned 2 arguments. Expected: 1"):
        functional_ops.For(0, 10, 1, [0.0], ReturnsTooManyArgs)[0].eval()
