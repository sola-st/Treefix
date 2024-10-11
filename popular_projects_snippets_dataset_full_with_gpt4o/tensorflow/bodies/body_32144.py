# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_format_op_test.py
with self.cached_session():
    with self.assertRaisesRegex(
        ValueError, r"The template expects 2 tensors, but the inputs only has"
        r" 1\.\s.*"):
        tensor = math_ops.range(10)
        format_output = string_ops.string_format("{} {}", tensor)
        self.evaluate(format_output)
with self.cached_session():
    with self.assertRaisesRegex(
        ValueError, r"The template expects 2 tensors, but the inputs only has"
        r" 1\.\s.*"):
        tensor = math_ops.range(10)
        format_output = string_ops.string_format("{} {}", [tensor])
        self.evaluate(format_output)
with self.cached_session():
    with self.assertRaisesRegex(
        ValueError, r"The template expects 1 tensors, but the inputs only has"
        r" 2\.\s.*"):
        tensor = math_ops.range(10)
        format_output = string_ops.string_format("{}", (tensor, tensor))
        self.evaluate(format_output)
