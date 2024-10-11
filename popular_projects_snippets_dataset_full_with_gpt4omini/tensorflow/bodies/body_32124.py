# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_format_op_test.py
with self.cached_session():
    tensor = math_ops.range(10)
    format_output = string_ops.string_format("{}", tensor)
    out = self.evaluate(format_output)
    expected = "[0 1 2 ... 7 8 9]"
    self.assertEqual(compat.as_text(out), expected)

with self.cached_session():
    tensor = math_ops.range(10)
    format_output = string_ops.string_format("{}", [tensor])
    out = self.evaluate(format_output)
    expected = "[0 1 2 ... 7 8 9]"
    self.assertEqual(compat.as_text(out), expected)
