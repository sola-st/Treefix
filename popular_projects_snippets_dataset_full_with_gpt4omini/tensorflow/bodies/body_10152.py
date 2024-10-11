# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
if context.executing_eagerly():
    error = errors_impl.InvalidArgumentError
    error_message = (
        r"cannot compute Add(V2)? as input #1\(zero-based\) was expected to "
        r"be a int32 tensor but is a float tensor \[Op:Add(V2)?\]")
else:
    error = TypeError
    error_message = (
        "Input 'y' of 'Add(V2)?' Op has type float32 that does not "
        "match type int32 of argument 'x'.")
with self.assertRaisesRegex(error, error_message):
    a = array_ops.ones([1], dtype=dtypes.int32) + 1.0
    self.evaluate(a)
